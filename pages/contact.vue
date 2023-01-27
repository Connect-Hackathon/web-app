<template>
    <div>
        <p>admin area</p>
        <div class="container row-1">
            <div v-for="people of peeps" :key="people.name">
                <p>{{ people.name }}</p>
            </div>
            
        </div>
    </div>

</template>

<script setup>
import formres from '../../server/assets/formres.json'
const auth = useAuth();
if(auth.value.isAuthenticated === false){
    navigateTo('/login')
}
const {data: peeps} = useFetch('/api/data')




</script>

<style lang="scss" scoped>

</style>