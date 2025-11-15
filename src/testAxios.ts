import axios from 'axios';

axios.get('https://jsonplaceholder.typicode.com/todos/1')
  .then(res => console.log(res.data))
  .catch(err => console.error(err));
