/*eslint-disable*/ 
export default function getResponseFromAPI(success) {
    const maPromise = new Promise((resolve, reject) => {
        if (success) {
          resolve({ status: 200, body: 'Success' });;
        } else {
            reject(new Error('The fake API is not working currently'));
        }
    });
    return maPromise;
}
