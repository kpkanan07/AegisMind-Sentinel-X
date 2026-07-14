import Navbar from "../components/Navbar";
import ThreatCard from "../components/ThreatCard";
import RiskScore from "../components/RiskScore";
import AlertPanel from "../components/AlertPanel";
import AIReasoningPanel from "../components/AIReasoningPanel";
import ThreatChart from "../components/ThreatChart";


function Dashboard(){

return(

<div className="dashboard">


<Navbar/>


<h1>
🛡️ Cyber Defense Command Center
</h1>


<span className="status">
SYSTEM ONLINE
</span>



<div className="grid">


<ThreatCard
title="Active Threats"
value="12"
/>


<RiskScore
score="78"
/>


<ThreatCard
title="AI Agents"
value="4"
/>


<ThreatCard
title="Network Status"
value="Secure"
/>



</div>



<br/>


<ThreatChart/>


<br/>


<div className="grid">

<AlertPanel/>

<AIReasoningPanel/>

</div>



</div>

)

}


export default Dashboard;