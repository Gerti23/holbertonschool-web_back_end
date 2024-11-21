// eslint-disable-next-line no-undef
module.exports = function getListStudentIds(arr) {
    if (!(arr instanceof Array)) { return []; }
  
    return arr.map((x) => x.id);
  };