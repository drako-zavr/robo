<template>
    <SectionBlock title="Выберите нужный пакет">
        <div class="q-container">
            <div class="row ">
                <!-- <PackageCard class="col-4"/>
    <PackageCard class="col-4"/>
    <PackageCard class="col-4"/> -->
                <div class="col-4-lg col-4-md col-12-sm centered">
                    <PackageCard 
                    title="– PRO –" 
                    price="20.000 ₽" 
                    desc="УМК по робототетхнике и программированию"
                    bgClass="package-card-active" />
                </div>
                <div class="col-4-lg col-4-md col-12-sm centered">
                    <PackageCard title="– ROBO –" price="15.000 ₽" desc="УМК по робототетхнике" />
                </div>
                <div class="col-4-lg col-4-md col-12-sm centered">
                    <PackageCard title="– PROG –" price="10.000 ₽" desc="УМК по программированию" />
                </div>
                <!-- <PackageCard />
    <PackageCard />
    <PackageCard /> -->
            </div>
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import PackageCard from './PackageCard.vue';
import SectionBlock from './SectionBlock.vue';
</script>