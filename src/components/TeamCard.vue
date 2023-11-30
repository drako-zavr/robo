<template>
    <q-card
    class="team-card flex column justify-start q-pa-md col">
    <!-- <img class="team-card__img" :src="teammate?.photo"> -->
    <q-avatar
      :size="`${$q.screen.lt.sm ? '100' : '200'}px`"
      v-if="teammate?.photo"
    >
      <img :src="teammate.photo" class="team-card__img" />
    </q-avatar>
    <!-- <img class="team-card__img" src="{{ photo }}"> -->
    <q-card-section>
        <p class="team-card__name">{{teammate?.name}}</p>
        <p class="team-card__position">{{teammate?.position}}</p>
        <a class="team-card__details">Подробнее</a> 
    </q-card-section>
    

  
    </q-card>  
    
</template>
<script setup lang="ts">
import { Teacher } from '../types/index';
import { PropType } from 'vue';
  // defineProps({
  //   photo: String,
  //   name: String,
  //   position: String,
  //   details: String
  // });
  defineProps({
    teammate: Object as PropType<Teacher>
  });
</script>