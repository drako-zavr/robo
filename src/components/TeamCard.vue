<template>
    <q-card
    class="team-card flex column justify-start q-pa-md col">
    
    <q-img class="team-card__img" v-if="teammate?.photo" :src="teammate.photo"
    :height="`${$q.screen.lt.sm ? '306' : '500'}px`"
    :width="`${$q.screen.lt.sm ? '306' : '500'}px`"
    />
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