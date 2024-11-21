const updateUniqueItems = require("./10-update_uniq_items.js");
const groceriesList = require("./9-groceries_list.js");

const map = groceriesList();
console.log(map);

updateUniqueItems(true)
console.log(map);