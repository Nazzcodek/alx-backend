import { createQueue } from 'kue';
import { createPushNotificationsJobs } from './8-job.js';

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
];

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  test('should throw error if jobs is not an array', () => {
    const invalidJobs = 'not_an_array';

    expect(() => createPushNotificationsJobs(invalidJobs, queue)).toThrowError('Jobs is not an array');
  });

  test('should create jobs in the queue', () => {
    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).toBe(jobs.length);
    jobs.forEach((jobData, index) => {
      const job = queue.testMode.jobs[index];
      expect(job.type).toBe('push_notification_code_3');
      expect(job.data).toEqual(jobData);
    });
  });

});

