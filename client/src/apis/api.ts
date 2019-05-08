import axios from "axios"
import tokenState from '../utils/jwt'
import environ from '../config/prod'
import dev from '../config/dev'

//var ping = require('ping');


////127.0.0.1:5000/api/ 
//let url = 'http://192.168.88.159:5000/api/'
//let url = 'http://41.89.200.55/api/'
let url = 'http://127.0.0.1:5000/api/'
//let url = environ.API_URL;

//const API_URL = process.env.API_URL
//let URL1 = process.env.API_URL

//console.log("THE TEST ENVIRON::::::",environ.API_URL)


axios.defaults.headers.common["Access-Control-Allow-Origin"] = "23456agik" // for all requests
axios.defaults.headers.common['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Origin, Content-Type'
axios.defaults.headers.common['Access-Control-Max-Age'] = '5'
if (tokenState.isValidJwt(localStorage.getItem('tokenKey'))) {
    axios.defaults.headers.common['Authorization'] = localStorage.getItem('tokenKey')
}
else {
    axios.defaults.headers.common['Authorization'] = 'loginrequired'
}
export default {

    async getEntries(urlpath: any) {
        let data: any
        await axios
            .get(url + urlpath)
            .then(res => {

                //console.log("THE RESULT AT API ",res)

                data = res.data.result

            })
            .catch(error => {
                // eslint-disable-next-line
                console.log(error);
            })
        return data
    },

    async addEntry(urlpath: any, payload: any) {
        
        let data: any
        console.log("AT API ",payload)
        await axios
            .post(url + urlpath, payload)
            .then(res => {
                data = res;
            })
            .catch(error => {
                // eslint-disable-next-line
                console.error(error);
            })
        return data

    },
    async corsChecker(urlpath: any) {
        let data: any
        await axios
            .get(url + urlpath)
            .then(res => {
                data = res.data
            })
            .catch(error => {
                console.error(error);
            })
        return data

    },
    async editEntry(urlpath: any, id: any, payload: any) {
        let data: any
        await axios
            .put(url + urlpath + '/' + id, payload)
            .then(res => {
                data = res
            })
            .catch(error => {
                console.log(error);
            })
        return data
    },
    async deleteEntry(urlpath: any, id: any, payload: any) {
        let data: any
        await axios
            .delete(url + urlpath + '/' + id, payload)
            .then(res => {
                data = res
            })
            .catch(error => {
                console.log(error);
            })
        return data
    },
    async getEntry(urlpath: any, searchValue: any) {
        console.log("APT API ::: ", searchValue)
        let data: any
        await axios
            .get(url + urlpath + '/' + searchValue)
            .then(res => {
                data = res
               // console.log(data)
            })
            .catch(error => {
                console.log(error);
            })
        return data
    },


    async getSingleEntry(urlpath: any, recordid: any) {
        let data: any
        
        await axios
            .get(url + urlpath + '/' + recordid)
            .then( res => {
                data = res;
            })
            .catch(error => {
                console.log(error)
            })

        return data
    },


    async loginUser(urlpath: any, payload: any) {
        let data: any  
        
        await axios
            .post(url + urlpath, payload)
            .then(res => {
                // localStorage.removeItem('tokenKey') 
                console.log("LOGIN AT API ::::: ",res)                       
                if (res.data.login_state == "Login successful") {
                    localStorage.removeItem('userSession')
                    localStorage.removeItem('tokenKey');
                    localStorage.removeItem('userSessionPayroll');
                    data = res
                    console.log("THE TESPONSE ", res.data)
                    const receivedToken = res.data.token;
                    console.log("At api 222 ", receivedToken)
                    localStorage.setItem('tokenKey', receivedToken); 
                    axios.defaults.headers.common['Authorization'] = localStorage.getItem('tokenKey');
                    localStorage.setItem('userSession', res.data.user_details.designation);
                    localStorage.setItem('userSessionPayroll', res.data.user_details.payroll_no);
                    console.log("AT LOGIN ::::::::::::::*********", localStorage.getItem('userSession'))
                }  else if (res.data.login_state == "False"){
                    data = res.data.login_state;

                } else {
                    data = null
                }

            })
            .catch(error => {
                console.log(error);
            })
        

        return data
    },

    async checkBackendConn() {
        console.log("THE axio")
        let result: any
        await axios.get(url)
        .then(data => {
            if (data) {
              return  true


            } else {
                return false

            }
        }).catch(error => {
            return false
           
           
        })
       
    },


}
