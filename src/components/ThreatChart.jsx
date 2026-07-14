import {
LineChart,
Line,
XAxis,
YAxis
}
from "recharts";


const data=[

{
name:"10AM",
risk:30
},

{
name:"11AM",
risk:70
},

{
name:"12PM",
risk:90
}

];


function ThreatChart(){


return (

<div className="card">


<LineChart
width={400}
height={250}
data={data}>


<XAxis dataKey="name"/>

<YAxis/>

<Line
dataKey="risk"
/>


</LineChart>


</div>

)

}


export default ThreatChart;