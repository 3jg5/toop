/* رَفَدَ — محتوى الموقع المشترك (يُحمَّل لكل الزوار من Firestore) */
(function(){
'use strict';
var CFG=window.RAFAD_FB||{}, CACHE='rafad_content_v1';
var DOC_URL=CFG.projectId?'https://firestore.googleapis.com/v1/projects/'+CFG.projectId+'/databases/(default)/documents/site/content':'';

/* ---------- استخراج النصوص القابلة للتعديل (مشترك مع صفحة الإدارة) ---------- */
function leaves(root){
  var out=[],els=root.querySelectorAll('body *');
  for(var i=0;i<els.length;i++){
    var el=els[i],tag=el.tagName.toLowerCase();
    if(/^(script|style|svg|noscript|path|use|br|canvas|button|template)$/.test(tag))continue;
    if(el.closest('svg,.member,script,style,[data-noedit]'))continue;
    if(el.children.length)continue;
    if(el.hasAttribute('data-to')||/(^|\s)(n|plus)(\s|$)/.test(el.className||''))continue;
    var t=(el.dataset&&el.dataset.rfO)||el.textContent.trim();
    if(t.length<2)continue;
    out.push({el:el,text:t});
  }
  return out;
}
function avatar(n){
  n=(n||'').replace(/^الأستاذ\s+/,'').replace(/^ال/,'');
  return n.charAt(0)||'•';
}

/* ---------- تطبيق المحتوى ---------- */
function apply(c){
  if(!c)c={};
  /* النصوص */
  var map={};(c.texts||[]).forEach(function(x){if(x&&x.o)map[x.o]=x.t});
  leaves(document).forEach(function(l){
    var el=l.el,o=l.text;
    if(Object.prototype.hasOwnProperty.call(map,o)&&map[o]!==o){
      if(!el.dataset.rfO)el.dataset.rfO=o;
      el.textContent=map[o];
    }else if(el.dataset.rfO&&el.textContent!==el.dataset.rfO){
      el.textContent=el.dataset.rfO;
    }
  });
  /* الأرقام */
  var nums=document.querySelectorAll('[data-to]');
  var nm={};(c.nums||[]).forEach(function(x){if(x)nm[x.i]=x});
  for(var i=0;i<nums.length;i++){
    var n=nums[i];if(!n.dataset.rfO)n.dataset.rfO=n.dataset.to;
    var x=nm[i],want=(x&&String(x.o)===n.dataset.rfO&&isFinite(+x.to))?String(+x.to):n.dataset.rfO;
    if(n.dataset.to!==want){
      n.dataset.to=want;
      if(n.textContent.trim()!=='0')n.textContent=(n.dataset.pre||'')+Math.round(+want).toLocaleString('en-US')+(n.dataset.suf||'');
    }
  }
  /* الفريق */
  var tm=c.team;if(!tm)return;
  var sup=document.querySelector('.member.sup'),grid=document.querySelector('#team .team');
  if(sup&&tm.sup){
    sup.querySelector('h3').textContent=tm.sup;
    sup.querySelector('.av').textContent=avatar(tm.sup);
    if(tm.supRole)sup.querySelector('.role').textContent=tm.supRole;
  }
  if(grid&&Array.isArray(tm.members)&&tm.members.length){
    var cards=grid.querySelectorAll('.member');
    tm.members.forEach(function(m,i){
      var a=cards[i];
      if(!a){a=cards[0].cloneNode(true);a.classList.add('in');grid.appendChild(a)}
      a.querySelector('.av').textContent=avatar(m.n);
      a.querySelector('h3').textContent=m.n;
      a.querySelector('p').textContent=m.r||'';
    });
    for(var j=cards.length-1;j>=tm.members.length;j--)cards[j].remove();
  }
}

/* ---------- تحميل ---------- */
function getCache(){try{return JSON.parse(localStorage.getItem(CACHE)||'null')}catch(e){return null}}
function setCache(c){try{localStorage.setItem(CACHE,JSON.stringify(c))}catch(e){}}
function fetchRemote(){
  if(!DOC_URL)return Promise.reject(new Error('no-config'));
  return fetch(DOC_URL+'?t='+Date.now(),{cache:'no-store'}).then(function(r){
    if(r.status===404)return {};
    if(!r.ok)throw new Error('http '+r.status);
    return r.json();
  }).then(function(d){
    var s=d&&d.fields&&d.fields.json&&d.fields.json.stringValue;
    return s?JSON.parse(s):{};
  });
}
window.RafadContent={leaves:leaves,avatar:avatar,apply:apply,fetchRemote:fetchRemote,DOC_URL:DOC_URL};
if(window.RAFAD_ADMIN)return;

apply(getCache());
fetchRemote().then(function(c){setCache(c);apply(c)}).catch(function(){});

/* ---------- مدخل الإدارة المخفي: 5 نقرات سريعة على شعار التذييل ---------- */
var logo=document.querySelector('.foot-logo'),taps=0,tt;
if(logo)logo.addEventListener('click',function(){
  taps++;clearTimeout(tt);tt=setTimeout(function(){taps=0},1500);
  if(taps>=5){taps=0;location.href='admin.html'}
});
})();