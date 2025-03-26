/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    for (let value of array) {
        array = appendString + value;
    }
    return array;
  }