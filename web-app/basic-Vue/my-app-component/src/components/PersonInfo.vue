<template>
    <CardCustom>
        <h1>name : {{ name }}</h1>
        <button @click="showDescription(id)">Details</button>&nbsp;
        <button @click="deleteEmployee(id)">Delete</button>
        <Transition name="fade">
            <div v-show="isVisible">
                <p>Salary : ${{ salary }}, Position: {{ department }}</p>
            </div>
        </Transition>

    </CardCustom>
</template>

<script>
import CardCustom from "./CardCustom.vue"

export default {

    name: "PersonInfo",
    components: {
        CardCustom
    },
    // data(){
    //     return{
    //         message:"Employ Info Details"
    //     }
    // },
    // props:["name", "salary"]

    // validate props
    props: {
        id: {
            type: Number,
        },
        name: {
            type: String,
            required: true,
        },
        salary: {
            type: Number,
            required: true,
            default: 1500,
        },
        department: {
            type: String,
            required: true,
            // default:1500,            
        },
        isVisible: {
            type: Boolean
        }
    },
    methods: {
        showDescription(id) {
            // console.log(id)
            this.$emit("show", id)
        },
        deleteEmployee(id) {
            this.$emit("deleteEMP", id)
        }
    }
}
</script>

<style scoped>
/* li{
    margin: 1rem 0;
    font-size: 1.25rem;
    font-weight: bold;
    background: #8ddba4;
    padding: 0.5rem;
    border-radius: 25px;
} */
button {
    font: inherit;
    cursor: pointer;
    border: 1px solid #ff0077;
    background: #ff0077;
    color: white;
    padding: 0.05rem 1rem;
    box-shadow: 1px 2px rgba(0, 0, 0, 0.26);
}

.fade-enter-from {
    opacity: 0;
}

.fade-enter-active {
    transition: all 0.5s linear;
}
</style>