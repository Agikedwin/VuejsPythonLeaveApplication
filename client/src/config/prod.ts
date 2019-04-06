// prod.env.js
'use strict'  
const merge = require('webpack-merge')
export default {  
  NODE_ENV: '"production"',
  API_URL: JSON.stringify("http://127.0.0.1:5000/api"),
  merge:merge,
  terd:process.env.BASE_URL
}