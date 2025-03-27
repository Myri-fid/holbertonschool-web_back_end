/* eslint-disable */
export default class Building {
    constructor(sqft) {
        if (typeof sqft !== 'number') {
            throw new TypeError('Sqft must be a number');
        }
        if (new.target === Building) {
            throw new Error('Building is an abstract class and cannot be instantiated directly');
        }
        this._sqft = sqft;

    }
    get sqft() {
        return this._sqft;
    }
    evacuationWarningMessage() {
        throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
}
