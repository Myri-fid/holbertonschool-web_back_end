/* eslint-disable */
export default class Currency {
    constructor(code, name) {
    this._code = code;
    this._name = name;
    }

    get code() {
        return this._code;
    }
    set code(value) {
        if (typeof value !== 'string') {
            throw new TypeError('code must be a string');
        }
        return this._code = value;
    }
    get name() {
        return this._name;
    }
    set name(value) {
        if (typeof value !== 'string') {
            throw new TypeError('name must be a string');
        }
        return this._name = value;
    }

    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }
}