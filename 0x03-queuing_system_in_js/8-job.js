const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error("Jobs is not an array");
  }
  for (const job of jobs) {
    const save = queue.create("push_notification_code_3", job);
    save.on("enqueue", () => {
      console.log(`Notification job created: ${save.id}`);
    }).on("complete", () => {
      console.log(`Notification job ${save.id} completed`);
    }).on("failed", (err) => {
      console.log(`Notification job ${save.id} failed: ${err}`);
    }).on("progress", (prct) => {
      console.log(`Notification job ${save.id} ${prct}% complete`);
    }).save();
  };
};

export default createPushNotificationsJobs;
