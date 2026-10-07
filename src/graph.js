// Only real campus locations are user-selectable. Road/intersection nodes are
// hidden inside the backend routing graph.
export const locations={
 gym:{id:'gym',name:'Amrita Gym',x:193,y:557},
 asb:{id:'asb',name:'ASB Hostel',x:343,y:477},
 engineering:{id:'engineering',name:'Amrita School of Engineering',x:431,y:418},
 itcanteen:{id:'itcanteen',name:'IT Canteen',x:416,y:330},
 girls:{id:'girls',name:'Amrita Girls Hostel',x:482,y:166},
 vidyalayam:{id:'vidyalayam',name:'Amrita Vidyalayam School',x:571,y:376},
 auditorium:{id:'auditorium',name:'Auditorium',x:712,y:367},
 children:{id:'children',name:"Children's Hostel",x:592,y:396},
 hanger:{id:'hanger',name:'Hanger Lab',x:820,y:470},
 kashyapa:{id:'kashyapa',name:'Kashyapa Bhavanam',x:904,y:463},
 sriVyasa:{id:'sriVyasa',name:'Sri Vyasa Maharishi Bhavanam',x:907,y:571},
 main:{id:'main',name:'Main Campus',x:726,y:602},
 cafe:{id:'cafe',name:"BRN Bhai's Cafe",x:300,y:788}
};


export const roadNodes = {
  engineering:[431,418], itcanteen:[416,330], girls:[482,166],
  vidyalayam:[571,376], auditorium:[712,367], children:[592,396],
  hanger:[820,470], kashyapa:[904,463], sriVyasa:[907,571],
  main:[726,602], gym:[193,557], asb:[343,477], cafe:[300,788],
  r_e1:[448,418], r_e2:[478,417], r_e3:[515,405], r_e4:[545,391],
  r_i1:[424,372], r_i2:[418,348], r_i3:[455,300], r_i4:[482,250], r_g1:[500,205],
  r_v1:[602,374], r_v2:[635,372], r_v3:[668,369], r_a1:[690,368],
  r_c1:[610,415], r_c2:[650,425], r_a2:[750,385], r_a3:[790,430],
  r_h1:[800,470], r_h2:[850,468], r_m1:[780,510], r_m2:[755,555],
  r_m3:[726,580], r_s1:[800,555], r_s2:[860,565], r_e5:[405,435],
  r_e6:[370,450], r_a4:[335,475], r_gym1:[310,500], r_gym2:[265,525],
  r_gym3:[225,545], r_cafe1:[250,620], r_cafe2:[275,700], r_cafe3:[290,755],
  r_main1:[470,470], r_main2:[520,505], r_main3:[575,535], r_main4:[635,565],
  r_main5:[685,585], r_main6:[760,615]
};
