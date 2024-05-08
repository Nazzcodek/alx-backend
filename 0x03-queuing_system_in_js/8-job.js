import { createQueue } from 'kue';

const queue = createQueue({ concurrent: 2 });

function createPushNotificationsJobs(jobs, queue) {
  if(!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

jobs.forEach((jobData, index) => {
  const job = queue.create('push_notification_code_3', jobData);

  job.on('enqueue', function() {
    console.log(`Notification job created: ${job.id}`);
  });

  job.on('complete', function() {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', function(error) {
    console.log(`Notification job ${job.id} failed: ${error}`);
  });

  job.on('progress', function(progress) {
    console.log(`Notification job ${job.id} ${progress} complete`);
  });

  job.save();
  });
}

module.exports = createPushNotificationsJobs;
