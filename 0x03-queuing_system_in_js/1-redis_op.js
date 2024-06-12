import {createClient, print} from "redis";

const client = createClient();

client.on("error", err => console.log(`Redis client not connected to the server: ${err}`));

client.on("connect", () => console.log("Redis client connected to the server"))

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (err, ans) => {
    console.log(ans);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
