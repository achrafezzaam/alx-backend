import { createClient, print } from "redis";

const client = createClient();

client.on("error", err => console.log(`Redis client not connected to the server: ${err}`));

const main = () => {
  const hash = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  }
  for (const [key, val] of Object.entries(hash)) {
    client.HSET('HolbertonSchools', key, val, print);
  }
  client.HGETALL('HolbertonSchools', (err, ans) => console.log(ans));
}

console.log(client.HGETALL('HolbertonSchools'));

client.on("connect", () => {
  console.log("Redis client connected to the server");
  main();
});
