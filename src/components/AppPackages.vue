<template>
    <SectionBlock id="price" title="Выберите нужный пакет">
        <div class="q-container q-mb-lg">
            <div class="row ">
                <!-- <div class="col-4-lg col-4-md col-12-sm q-mx-auto">
                    <PackageCard 
                    title="– PRO –" 
                    price="20.000 ₽" 
                    desc="УМК по робототетхнике и программированию"
                   />
                </div>
                <div class="col-4-lg col-4-md col-12-sm q-mx-auto">
                    <PackageCard title="– ROBO –" price="15.000 ₽" desc="УМК по робототетхнике" />
                </div>
                <div class="col-4-lg col-4-md col-12-sm q-mx-auto">
                    <PackageCard title="– PROG –" price="10.000 ₽" desc="УМК по программированию" />
                </div> -->
                <div v-for="pack in packagesList" :key="pack.id">
          <PackageCard :pack="pack" class="col" />
        </div>
            </div>
        </div> 
    </SectionBlock>
</template>
<script setup lang="ts">
import { usePackages } from 'src/composables/usePackages';
import PackageCard from './PackageCard.vue';
import SectionBlock from './SectionBlock.vue';
import { onMounted, ref } from 'vue';
import { Package } from '../models/package';


const { fetchPackages } = usePackages();
const packagesList = ref<Package[]>([]);
const isLoading = ref<boolean>(true);

onMounted(async () => {
  packagesList.value = await fetchPackages();
  isLoading.value = false;

});

</script>