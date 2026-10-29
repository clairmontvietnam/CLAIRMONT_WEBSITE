/* Clairmont Group — site script (multi-page) */
(function(){
  var D=document,$=function(id){return D.getElementById(id)};

  /* old single-page links (/#gioi-thieu …) → real pages */
  var OLD={'gioi-thieu':'/gioi-thieu/','nha-sang-lap':'/gioi-thieu/#nha-sang-lap','nang-luc':'/gioi-thieu/#nang-luc','dinh-huong':'/gioi-thieu/#dinh-huong',
    'linh-vuc':'/linh-vuc/','du-an':'/linh-vuc/#du-an','thuong-hieu':'/linh-vuc/#thuong-hieu','doi-tac':'/linh-vuc/#doi-tac','goc-nhin':'/goc-nhin/','lien-he':'/lien-he/'};
  var h=decodeURIComponent(location.hash.slice(1));
  if((location.pathname==='/'||location.pathname==='/index.html')&&OLD[h]){location.replace(OLD[h]);return}

  /* language VI / EN */
  var lang='vi';
  function set(l){lang=l;
    [].forEach.call(D.querySelectorAll('[data-en]'),function(e){if(!e.hasAttribute('data-vi'))e.setAttribute('data-vi',e.innerHTML);e.innerHTML=e.getAttribute(l==='en'?'data-en':'data-vi')});
    D.documentElement.lang=l;
    var a=$('l-vi'),b=$('l-en');if(a)a.setAttribute('aria-pressed',l==='vi');if(b)b.setAttribute('aria-pressed',l==='en');
    try{localStorage.setItem('clm-lang',l)}catch(e){}
  }
  if($('l-vi'))$('l-vi').onclick=function(){set('vi')};
  if($('l-en'))$('l-en').onclick=function(){set('en')};
  var saved=null;try{saved=localStorage.getItem('clm-lang')}catch(e){}
  if(saved==='en')set('en');

  /* background videos: play only when motion is allowed */
  if(!matchMedia('(prefers-reduced-motion:reduce)').matches){
    [].forEach.call(D.querySelectorAll('video.bgv'),function(v){var p=v.play();if(p&&p.catch)p.catch(function(){})});
  }

  /* mobile menu */
  var hd=$('hd'),mb=$('menu');
  if(hd&&mb){mb.onclick=function(){var o=hd.classList.toggle('open');mb.setAttribute('aria-expanded',o)};
    [].forEach.call(D.querySelectorAll('#nav a'),function(a){a.addEventListener('click',function(){hd.classList.remove('open');mb.setAttribute('aria-expanded','false')})});}

  /* copy email */
  function copyText(t,btn,node){
    var done=function(){var o=btn.textContent;btn.textContent=lang==='en'?'Copied':'Đã chép';setTimeout(function(){btn.textContent=o},1500)};
    var sel=function(){var r=D.createRange();r.selectNodeContents(node);var s=getSelection();s.removeAllRanges();s.addRange(r)};
    try{navigator.clipboard.writeText(t).then(done,sel)}catch(e){sel()}
  }
  var cm=$('copy-mail');
  if(cm)cm.onclick=function(){copyText($('mail').textContent,cm,$('mail'))};

  /* contact form — posts to window.CLM_FORM.endpoint when set, otherwise shows a copyable summary */
  var f=$('lead'),done=$('done');
  if(f)f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var n=f.name.value.trim(),p=f.phone.value.trim();
    if(!n||!p){done.hidden=false;done.textContent=lang==='en'?'Please enter your name and phone number.':'Vui lòng nhập họ tên và số điện thoại.';(n?f.phone:f.name).focus();return}
    var need=f.need.options[f.need.selectedIndex].text;
    var txt=(lang==='en'?'Name: ':'Họ tên: ')+n+'\n'+(lang==='en'?'Company: ':'Doanh nghiệp: ')+(f.org.value||'—')+'\n'+(lang==='en'?'Phone: ':'Điện thoại: ')+p+'\nEmail: '+(f.email.value||'—')+'\n'+(lang==='en'?'Interest: ':'Nhu cầu: ')+need+'\n'+(lang==='en'?'Message: ':'Nội dung: ')+(f.message.value||'—');
    function manual(){
      done.hidden=false;done.innerHTML='';
      var m=D.createElement('div');m.textContent=lang==='en'?'Thank you for your enquiry. Please send the details below to clairmontvietnam@gmail.com or call 0947 120 258.':'Cảm ơn Quý vị đã quan tâm. Vui lòng gửi nội dung dưới đây tới clairmontvietnam@gmail.com hoặc liên hệ 0947 120 258.';
      var pre=D.createElement('pre');pre.textContent=txt;
      var b=D.createElement('button');b.type='button';b.className='copy';b.style.marginLeft='0';b.textContent=lang==='en'?'Copy details':'Sao chép thông tin';
      b.onclick=function(){copyText(txt,b,pre)};
      done.appendChild(m);done.appendChild(pre);done.appendChild(b);
    }
    var ep=((window.CLM_FORM||{}).endpoint||'').trim();
    if(!ep){manual();return}
    var sb=f.querySelector('button[type=submit]');sb.disabled=true;
    var q=new URLSearchParams();[['name',n],['org',f.org.value],['phone',p],['email',f.email.value],['need',need],['message',f.message.value],['lang',lang],['page',location.href],['time',new Date().toISOString()]].forEach(function(kv){q.append(kv[0],kv[1]||'')});
    fetch(ep,{method:'POST',mode:'no-cors',body:q}).then(function(){sb.disabled=false;f.reset();done.hidden=false;done.textContent=lang==='en'?'Thank you. Your enquiry has been sent — Clairmont will be in touch shortly.':'Cảm ơn Quý vị. Thông tin đã được gửi — Clairmont sẽ liên hệ lại trong thời gian sớm nhất.'},function(){sb.disabled=false;manual()});
  });
})();
