export default class HolbertonCourse {
    constructor(name, length, students) {
      if (typeof (name) !== 'string' || typeof (length) !== 'number') {
        throw new Error();
      }
      if (!Array.isArray(students) || !students.every((student) => typeof (student) === 'string')) {
        throw new Error();
      }
  
      this._name = name;
      this._length = length;
      this._students = students;
    }
  
    get name() {
      return this._name;
    }
  
    set name(name) {
      if (typeof (name) !== 'string') throw new Error();
      this._name = name;
    }
  
    get length() {
      return this._length;
    }
  
    set length(length) {
      if (typeof (length) !== 'number') throw new Error();
      this._length = length;
    }
  
    get students() {
      return this._students;
    }
  
    set students(students) {
      if (!Array.isArray(students) || !students.every((student) => typeof (student) === 'string')) throw new Error();
      this._students = students;
    }
  }