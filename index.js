import server from 'server'

server.register('foo', 'bar');

server.login('foo', 'bar')
    .then(response => {
        console.log(response.data)
    })
    .catch(error => {
        console.log(error)
    });

server.logout();