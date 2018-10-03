<template>
  <div id="app">
    <b-navbar toggleable="md" type="light" variant="light">

      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

      <b-navbar-brand href="#">
        <h1 id="brand-text">
          <img src="/static/logo.png" class="logo">
          <span>Members Explorer</span>
        </h1>
      </b-navbar-brand>

      <b-collapse is-nav id="nav_collapse">
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <b-nav-item href="#" class="nav-items activated">Overview</b-nav-item>
            <b-nav-item href="#" class="nav-items">Explorer</b-nav-item>
          </b-navbar-nav>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'app',
    data() {
      return {
        loading: true,
        mapLoading: true,
      }
    },
    mounted() {
      this.loadMapMembers();
      this.loadFeatureMembers();
    },
    methods: {
      loadMapMembers() {

      },
      loadFeatureMembers() {

      }
    }
  }
</script>

<style lang="scss">
  #app {
    font-family: 'ABeeZee', sans-serif !important;
    letter-spacing: 2px;
    .navbar {
      height: 90px;
      #nav_collapse {
        background-color: #f8f9fa !important;
      }
    }
  }

  #brand-text {
    margin-left: 10%;
    margin-right: 50px;
    font-size: 15pt;
  }

  .logo {
    vertical-align: middle;
    width: 35px;
    height: 35px;
  }

  .nav-items {
    margin-right: 10px;
    margin-left: 10px;
    a.nav-link {
      color: #000000;
    }
  }

  .nav-items.activated {
    border-bottom: 2px solid #A3D165;
  }

</style>
