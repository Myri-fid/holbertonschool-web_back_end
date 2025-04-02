/*eslint-disable*/ 
export default function getResponseFromAPI() {
    const maPromise = new Promise((resolve, reject) => {
        const success = true;
        if (success) {
          resolve("status: 200, body: 'Success'");
        } else {
          reject("The fake API is not working currently");
        }
    });
    return maPromise;
}
