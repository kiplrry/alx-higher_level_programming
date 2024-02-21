#!/usr/bin/node

function call () {
  return new Promise((resolve) => {
    const j = [];
    setTimeout(() => {
      j.push(45);
      console.log(`set j ${j}`);
      resolve(j);
    }, 2000);
  });
}
async function receiver () {
  console.log('calling');
  const res = await call();
  return res;
}

const ol = call();
console.log(`j = ${ol}`);
receiver().then((res) => {
  console.log(`res = ${res}`);
}
);
