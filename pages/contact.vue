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


</script>

<style lang="scss" scoped>

</style>