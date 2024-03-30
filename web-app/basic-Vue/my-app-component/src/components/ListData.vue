<template>
    <!-- <div> -->
    <!-- <h1>{{ message }}</h1> -->
    <!-- <PersonInfo name="Rick" salary=1000 />
        <PersonInfo name="Morty" salary=2000 /> -->
    <ul>
        <!-- <CardCustom>
            First Employee
        </CardCustom> -->
        <PersonInfo 
        v-for="(item, index) in employee"
        :key="index" 
        :id="item.id"
        :name="item.name" 
        :salary="item.salary"
        :department="item.department" 
        :isVisible="item.isVisible"
        @show="toggleVisible"
        @deleteEMP="removeEMP"
        />
    </ul>
    <!-- </div> -->
</template>

<script>
// import PersonInfo from "./PersonInfo.vue";
import PersonInfo from "./PersonInfo.vue"
// import CardCustom from "./CardCustom.vue"
export default {
    name: "ListData",
    components: {
        PersonInfo,
        // CardCustom,
    },

    // props:["name"]
    // data(){
    //     return{
    //         message:"Show Employee Name"
    //     }
    // }

    // props:["employee"]
    data() {
        return {
            employee: [
                {id:1, name: "Rick-c137", salary: 1000, department:"Engineer", isVisible:false},
                {id:2, name: "Morty-c137", salary: 1000, department:"Engineer", isVisible:false},
                {id:3, name: "Rick-616", salary: 100, department:"Engineer" , isVisible:false},
                {id:4, name: "Morty-616", salary: 100, department:"Engineer" , isVisible:false},
                {id:5, name: "Rick-a217", salary: 10, department:"Engineer", isVisible:false },
                {id:6, name: "Morty-a217", salary: 10, department:"Engineer" , isVisible:false},
            ]
        }
    },
    methods:{
        toggleVisible(id){
            // console.log("child ID :", emp_id)
            this.employee = this.employee.map((item)=>{
                if(item.id === id){
                    return {...item, isVisible:!item.isVisible}
                }
                return item
            })
        },
        removeEMP(id){
            this.employee = this.employee.filter(item=>{
                return item.id !== id
            })
        }
    }
}
</script>

<style scoped>

ul{
    list-style: none;
    margin: 1rem 0;
    padding: 0;
}

</style>