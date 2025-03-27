/* eslint-disable */
export default class HolbertonCourse {
    constructor(name, length, students) {

        this._name = name;
        this._length = length;
        this._students = students;
    }
    get name() {
        return this._name;
    }
    set name(newname) {
        if (typeof newname != 'string') {
            throw new Error('nom dois etre un string');
        }
        this._name = newname;
    }
    get length() {
        return this._length;
    }
    set length(newlenght) {
        if (typeof newlenght != 'number') {
            throw new Error('lenght doit etre un nombre');
        }
        this._length = newlenght;
    }
    get students() {
        return this._students;
    }
    set students(newstudents){
        if (!Array.isArray(newstudents)) {
            throw new Error('student dois etre array of string');
        }
        this._students = newstudents;
    }
}