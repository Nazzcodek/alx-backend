import express form 'express';
import redis from 'redis';
import Kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = redis.createClient({
  host: 'localhost',
  port: 6379,
});

client.on('error', (err) => console.log('Redis Client Error', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;
let numberOfAvailableSeats = 50;

client.set('available_seats', numberOfAvailableSeats, 'EX', 60 * 60 * 24);

app.use(express.json());

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getAsync('available_seats');
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = Kue.create('reserve_seat', { number: 1 }).save((err) => {
    if (err) {
      console.error('Job creation failed:', err);
      return res.json({ status: 'Reservation failed' });
    }
    console.log('Seat reservation job', job.id, 'created');
    res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  Kue.jobs('reserve_seat', async (job) => {
    try {
      const currentSeats = await getAsync('available_seats');
      const newSeats = parseInt(currentSeats) - 1;
      await setAsync('available_seats', newSeats);
      if (newSeats <= 0) {
        reservationEnabled = false;
      }
      console.log(`Seat reservation job ${job.id} completed`);
    } catch (error) {
      console.error(`Seat reservation job ${job.id} failed: ${error.message}`);
    }
  });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

