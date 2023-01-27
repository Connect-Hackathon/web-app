<template>
    <div>
        <h1 class="h1 text-white text-center">Welcome to Connect 5's CV Screening service</h1>
        <p class="text-center text-white">Please fill out the form below to enter</p>
        <div id="form-internal-container">
            
        </div>

    </div>
</template>

<script setup>
import { useRuntimeConfig } from 'nuxt/app'
import { loadStripe } from '@stripe/stripe-js'
import formres from '../server/assets/formres.json';
import { ref } from 'vue';
const form = reactive({
    name: ref(''),
    email: ref(''),
    gender: ref(''),
    stunum: ref(''),
    phonum: ref(''),
    skill: ref(''),
    partname: ref(''),
    partemail: ref(''),
    partgender: ref(''),
    partstunum: ref(''),
    partphonum: ref(''),
    partskill: ref(''),
    ent: ref(''),
    price: ref('')

})


async function writetocsv() {
    // run payment

    //if payment = bad
 /* 
    
    
    

      async takePayment() {
        const config = useRuntimeConfig()
        const stripe = await loadStripe(config.public.stripePk)
        //WE DONT NEED AS PRICE SHOULD BE IF FORM.ENT === SOLO PRICE = 14 or a similar directive
        const lineItems = []
        this.items.forEach(cartItem => {
          lineItems.push({
            price: cartItem.stripePriceId,
            quantity: cartItem.quantity,
          })
        })
        //THIS REDIRECTS TO STRIPE WEBSITE AND DOES PAYMENT
        const { error } = await stripe.redirectToCheckout({
          lineItems: lineItems,
          mode: 'payment',
          successUrl: `${config.public.appUrl}/success`,
          cancelUrl: `${config.public.appUrl}`,
        })
      }
    
    */




    /* if (payment=good) {
            const {data} = await useFetch(formres,{
            method: 'post', 
            body: {name:form.name,email:form.email,gender:form.gender, studentNumber: form.stunum,
                phoneNumber: form.phonum, skill: form.skill}
            });
        }
    */
   
}
async function writetojson() {
    const {data} = await useFetch("/api/write",{
            method: 'post', 
            body: {name:form.name,email:form.email,gender:form.gender, studentNumber: form.stunum,
                phoneNumber: form.phonum, skill: form.skill}
            });
    }

</script>

<style scoped>
.myForm {
    width: 300px;
}
</style>