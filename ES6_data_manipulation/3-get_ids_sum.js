/* eslint-disable */
export default function getStudentIdsSum(students) {
    return students.reduce((item, student) => item + student.id, 0);
  }
