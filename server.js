import axios from 'axios';


const server = {
    login: (username, password) => {},
    logout: () => {},
    register: (username, password, age=20) => {},
};

Object.keys(server).forEach(func => {
    server[func] = function () {
        return wrapper(func, arguments);
    }
});

function wrapper(func, _args) {
    return new Promise((resolve, reject) => {
        const args = [];
        for (let i = 0; i < _args.length; i++)
            args.push(_args[i])
        const url = '/path/to/api';
        axios.post(url, {func, args}
        ).then(response => {
            resolve(response)
        }).catch(error => {
                reject(error)
            }
        );
    });
}


export default server
