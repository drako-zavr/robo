<template>
    <SectionBlock title="Что вы получите после курса" bgClass="bg-dark">
        <div class="q-container result">
            <div class="row">

                <div class="col-lg-4 col-md-4 col-sm-12 q-px-md">
                    <p class="result__title text-secondary q-mb-md">Удостоверение</p>
                    <p class="result__text text-secondary">Дающее право преподавать робототехнику для детей 6-12 лет в образовательных
                        учреждениях</p>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 q-px-md">
                    <p class="result__title text-secondary q-mb-md">Знания</p>
                    <p class="result__text text-secondary">По основам разработки учебно-методических комплексов
                        по робототехнике и программированию</p>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-12 q-px-md">
                    <div class="result_practice row">
                        <p class="result__title text-secondary q-mb-md">Практику 
                            <q-tooltip  class="tooltip text-weight-regular text-center q-pt-md bg-primary text-secondary shadow-4" anchor="top middle" self="bottom middle" > 
                                При наличии свободных мест
                            </q-tooltip>
                        <img src="../assets/images/tooltip_i.svg"
                            class="tooltip-img">
                        </p>
                    </div>
                    <p class="result__text text-secondary">Возможность пройти практику по преподаванию робототехники на базе R:ED LAB (в
                        оффлайн или онлайн формате)</p>
                </div>

            </div>
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>