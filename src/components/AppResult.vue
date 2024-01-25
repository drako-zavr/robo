<template>
    <SectionBlock title="Что вы получите после курса" bgClass="bg-dark">
        <div class="q-container result row">
            <div class="col-lg-4 col-md-4 col-sm-12 q-px-md q-pb-xl">
                <p class="result__title text-secondary q-mb-md text-h5 text-weight-bold">Удостоверение</p>
                <p class="result__text text-secondary text-subtitle1">Дающее право преподавать робототехнику для детей 6-12 лет в образовательных учреждениях</p>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-12 q-px-md q-pb-xl">
                <p class="result__title text-secondary q-mb-md text-h5 text-weight-bold">Знания</p>
                <p class="result__text text-secondary text-subtitle1">По основам разработки учебно-методических комплексов
                    по робототехнике и программированию</p>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-12 q-px-md q-pb-xl">
                    <p class="result__title text-secondary q-mb-md relative-position text-h5 text-weight-bold">Практику
                        <q-tooltip
                            class="tooltip text-weight-regular text-center q-pt-md bg-primary text-secondary shadow-4 text-subtitle1"
                            anchor="top middle" self="bottom middle">
                            При наличии свободных мест
                        </q-tooltip>
                        <img src="../assets/images/tooltip_i.svg" class="absolute q-ml-sm">
                    </p>
                <p class="result__text text-secondary text-subtitle1">Возможность пройти практику по преподаванию робототехники на базе
                    R:ED LAB (в оффлайн или онлайн формате)</p>
            </div>
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>