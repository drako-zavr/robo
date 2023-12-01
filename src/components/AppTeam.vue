<template>
  <SectionBlock title="Профессиональные тренеры">
   
      <q-scroll-area
       style="height: 700px; max-width: 100%;"
       
       >
      <div class="row no-wrap">
        <div class="col" style="width: 380px;"></div>

        <div v-for="teammate in teammatesList" :key="teammate.id" >
          <TeamCard v-if="teammate.display" :teammate="teammate" class="col" />
        </div>
        <div class="col" style="width: 380px;"></div>
      </div>
      </q-scroll-area>
      <img src="../assets/images/arrow_left.svg">
      <img src="../assets/images/arrow_right.svg">
 
    <!-- <q-btn class="arrow-btn"></q-btn> -->
  </SectionBlock>
</template>
<script setup lang="ts">
import TeamCard from './TeamCard.vue';
import SectionBlock from './SectionBlock.vue';
// import { useTeam } from '../hooks';
import { onMounted, ref } from 'vue';
import { Teacher } from '../types/index';
import { api } from 'boot/axios';
// import { LocationQuery } from 'vue-router';

function useTeam() {
  const fetchTeam = async () => {
    try {
      const { data } = await api.get<Teacher[]>('/team/list');
      return data;
    } catch (error) {
      console.error(error);
    }
    return [];
  };
  return {
    fetchTeam
  };
}
// function useTeam() {
//   const fetchTeamList = (query: LocationQuery): Promise<Teacher[]> => {
//     return new Promise((resolve, reject) => {
//       api
//         .get<Teacher[]>('team/list/', { params: query })
//         .then((response) => {
//           resolve(response.data);
//         })
//         .catch((error) => {
//           console.error(error);
//           reject(error);
//         });
//     });
//   };
// //   const fetchArticleDetails = (
// //     articleId: number | string
// //   ): Promise<Teacher> => {
// //     return new Promise((resolve, reject) => {
// //       api
// //         .get<Teacher>(`article/details/${articleId}`)
// //         .then((response) => {
// //           resolve(response.data);
// //         })
// //         .catch((error) => {
// //           console.error(error);
// //           reject(error);
// //         });
// //     });
// //   };

//   return {
//     fetchTeam
//     // fetchArticleDetails
//   };
// }


const { fetchTeam } = useTeam();

const teammatesList = ref<Teacher[]>([]);
const isLoading = ref<boolean>(true);

onMounted(async () => {
  teammatesList.value = await fetchTeam();
  isLoading.value = false;
});



</script>