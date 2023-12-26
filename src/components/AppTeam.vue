<template>
  <SectionBlock id="teachers" title="Профессиональные тренеры">

    <q-scroll-area class="team-scroll" ref="scrollAreaRef" 
    bar-style=null
    :height="`${$q.screen.lt.sm ? '500' : '700'}px`"
    :style="`${$q.screen.lt.sm ? 'height: 500' : 'height: 700'}px`"
    >

      <div class="row no-wrap">
        <div class="col" style="width: 10vw;"></div>
        <div v-for="teammate in teammatesList" :key="teammate.id">
          <TeamCard :teammate="teammate" class="col" />
        </div>
        <div class="col" style="width: 10vw;"></div>
      </div>

    </q-scroll-area>
    <div class="btns row">
      <q-img class="arrow-btn" src="../assets/images/arrow_left.svg"  @click="scrollLeft"></q-img>
      <q-img class="arrow-btn" src="../assets/images/arrow_right.svg" @click="scrollRight"></q-img>
    </div>

  </SectionBlock>

</template>
<script setup lang="ts">
import TeamCard from './TeamCard.vue';
import SectionBlock from './SectionBlock.vue';
import { onMounted, ref } from 'vue';
import { Teacher } from '../models/teacher';
import { useTeam } from '../composables/useTeam';


const { fetchTeam } = useTeam();
const teammatesList = ref<Teacher[]>([]);
const isLoading = ref<boolean>(true);

onMounted(async () => {
  teammatesList.value = await fetchTeam();
  isLoading.value = false;

});


// scroll team
const position = ref(300)
const scrollAreaRef = ref(null)

const scrollLeft = () =>  {
  position.value = 0
  scrollAreaRef.value.setScrollPosition('horizontal', position.value, 300)
}

const scrollRight = () => {
  position.value += 500
  scrollAreaRef.value.setScrollPosition('horizontal', position.value,300)
}

</script>