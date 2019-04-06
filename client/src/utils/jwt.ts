import Vue from 'vue'
import jwt_decode from 'jwt-decode';
//import * as JWT from 'jwt-decode';

export const EventBus = new Vue()

export default {
    isValidJwt(jwt: any) {
        if (!jwt || jwt.split('.').length < 3) {
            return false
        } else {
            
            const data = JSON.parse(atob(jwt.split('.')[1]))
            const exp = new Date(data.exp * 1000) // JS deals with dates in milliseconds since epoch
            const now = new Date()
            //const decode_token = jwt_decode(jwt);
            //console.log("JWT TOKEN  :",decode_token)
            if (now < exp) {
                return true
            }
            return false
        }

    },

    getUserSession(){
       const  userid= localStorage.getItem('userSession')
       console.log("the user Id ::::",userid )
    }

}


