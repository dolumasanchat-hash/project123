const obj = {
  first: function() { return 1; },
  second: function() { return 2; },
  third: function() { return 3; }
};

for (const key in obj) {
    console.log(obj[key]());
}