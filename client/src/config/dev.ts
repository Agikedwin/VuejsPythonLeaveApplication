// dev.env.js

'use strict'  
const merge = require('webpack-merge')  

export default  merge( {  
  NODE_ENV: '"development"',
  API_URL: JSON.stringify(`http://localhost:5000/`)
})