<template>
    <div>
        <h1>Login to admin</h1>
    <span v-if="_error" class="alert alert-danger">{{_error}}</span>
    <form @submit.prevent="deetcheck">
        <input class="form-control width: 120px" v-model="form.username" type="text" placeholder="Username"><br>
        <input class="form-control width: 120px" v-model="form.password" type="password" placeholder="Password"><br>
        <button class="btn btn-primary" type="submit">Login</button>
    </form>
    </div>
</template>

<script setup>
import {ref} from 'vue';
const form = reactive({
    username: ref(''),
    password: ref(''),
})
const auth = useAuth();
const _error = ref('');

async function deetcheck() {

const {data,error} = await useFetch('/api/deetcheck',{method: 'post', body:{username: form.username, password: form.password}});
if(data.value.data === "sucess"){
   
    auth.value.isAuthenticated=true
    navigateTo('/admin')
}else{
    _error.value = "Incorrect details entered";
}
}

</script>

<style scoped>

</style>