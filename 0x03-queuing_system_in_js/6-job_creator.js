const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '08051973456',
  message: 'this is the message you get for notification',
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', function() {
  console.log(`Notification job created:${job.id}`);
});

job.on('complete', function() {
  console.log('Notification job completed');
});

job.on('failed', function() {
  console.log('Notification job failing');
});

job.save();
