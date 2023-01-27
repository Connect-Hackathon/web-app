<template>
    <nav id="navbar" class="navbar navbar-expand-md navbar-light shadow-sm">
        <div class="container">
            <a class="navbar-brand" href="#">
                <img src="~/assets/images/icon.png" style="height: 40px; width: auto;"
                    class="d-inline-block align-text-center">
                Connect 5 CV Screening
            </a>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">

                <ul class="navbar-nav ms-auto">
                    <li class="nav-item dropdown">
                        <a id="navbarDropdown" class="nav-link dropdown-toggle text-white" href="#" role="button"
                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>Welcome Admin</a>
                        <div class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="#">
                                Dashboard
                            </a>
                            <a class="dropdown-item" href="#">
                                Logout

                            </a>

                        </div>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <NuxtLink style="margin-right: 10px;" class="btn btn-secondary text-card-bg" to="/">Home</NuxtLink>
                        <NuxtLink style="margin-right: 10px;" class="btn btn-secondary text-card-bg" to="/about">About</NuxtLink>
                        <NuxtLink style="margin-right: 10px;" class="btn btn-secondary text-card-bg" to="/contact">Contact</NuxtLink>
                       <NuxtLink class="btn btn-primary text-card-bg" to="/admin">Login</NuxtLink>
                       <NuxtLink v-if="auth.isAuthenticated===true"  style="margin-left: 10px;" class="btn btn-primary text-card-bg" to="/" @click.prevent="logout">Logout</NuxtLink>

                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script setup>
const auth = useAuth();
function logout() {
    auth.value.isAuthenticated = false;
}


</script>
