<template>
  <q-page class="index-page">
    <AppHeader/>
    <!-- <AppExample/> -->
    <AppInfo/>
    <AppResult/>
    <AppTeam/> 
    <AppPackages/>
    <AppFeedback/>
    
  </q-page>
</template>

<script setup lang="ts">
// import AppExample from 'components/AppExample.vue'
import AppFeedback from 'src/components/AppFeedback.vue';
import AppHeader from 'src/components/AppHeader.vue';
import AppTeam from 'src/components/AppTeam.vue';
import AppPackages from 'src/components/AppPackages.vue';
import AppInfo from 'src/components/AppInfo.vue';
import AppResult from 'src/components/AppResult.vue';
</script>
