<!DOCTYPE html>
<!-- saved from url=(0095)https://colab.research.google.com/drive/1PCga96CMC_NQg61iq2IiLVF7R0IXtb7w#scrollTo=3ptW1KTEGXoA -->
<html lang="en" theme="dark" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><script type="text/javascript" async="" charset="utf-8" src="./APP.py - Colab_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-1hXncclAK9oddvNk7nwUp8lOZ2IQZ8EORLvz9K99Lac8WLGSbW6clTN1YX0NyXHn" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./APP.py - Colab_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-1hXncclAK9oddvNk7nwUp8lOZ2IQZ8EORLvz9K99Lac8WLGSbW6clTN1YX0NyXHn" nonce=""></script><script type="text/javascript" async="" src="./APP.py - Colab_files/js" nonce=""></script><script src="./APP.py - Colab_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./APP.py - Colab_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./APP.py - Colab_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>APP.py - Colab</title><link href="./APP.py - Colab_files/css2" rel="stylesheet"><link href="./APP.py - Colab_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_3d{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Qa:hover::after,a.gb_Qa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua{background:#f8f8f8}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ua{cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_H:active,#gb .gb_Va.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_dd{display:inline-block;vertical-align:middle}.gb_Oe .gb_Q{bottom:-3px;right:-5px}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_ed{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_fd{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_fd{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_dd.gb_Uc .gb_ed,.gb_dd.gb_Uc .gb_fd,.gb_dd.gb_Uc .gb_la,.gb_Uc.gb_la{display:block}.gb_dd.gb_Uc.gb_gd .gb_ed,.gb_dd.gb_Uc.gb_gd .gb_fd{display:none}.gb_Pe{position:absolute;right:8px;top:62px;z-index:-1}.gb_hd .gb_ed,.gb_hd .gb_fd,.gb_hd .gb_la{margin-top:-10px}.gb_dd:first-child,#gbsfw:first-child+.gb_dd{padding-left:4px}.gb_Fa.gb_Qe .gb_dd:first-child{padding-left:0}.gb_Re{position:relative}.gb_3c .gb_Re,.gb_Kd .gb_Re{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_id:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_jd button svg,.gb_B{-webkit-border-radius:50%;border-radius:50%}.gb_jd button:focus:not(:focus-visible) svg,.gb_jd button:hover svg,.gb_jd button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_Mc .gb_jd button:focus-visible svg,.gb_Mc .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_Mc .gb_jd button:focus-visible svg{outline:1px solid currentcolor}}.gb_Mc .gb_jd.gb_kd button:focus svg,.gb_Mc .gb_jd.gb_kd button:focus:hover svg,.gb_jd button:focus svg,.gb_jd button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Mc .gb_jd.gb_kd button:active svg,.gb_jd button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_Mc .gb_jd.gb_kd button:hover svg,.gb_jd button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_B.gb_Za:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_Mc .gb_jd button:hover svg,.gb_Mc .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_Mc .gb_jd button:focus svg,.gb_Mc .gb_jd button:focus:hover svg,.gb_Mc .gb_B:focus,.gb_Mc .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Mc .gb_jd button:active svg,.gb_Mc .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_Mc .gb_B[aria-expanded=true],.gb_Mc .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Mc .gb_B[aria-expanded=true] .gb_F{fill:#fff;opacity:1}.gb_dd{padding:4px}.gb_Fa.gb_Qe .gb_dd{padding:4px 2px}.gb_Fa.gb_Qe .gb_z.gb_dd{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_ld{left:0;right:auto}@media (max-width:350px){.gb_la.gb_ld{left:0}}.gb_Se .gb_la{top:56px}.gb_R{display:none!important}.gb_od{visibility:hidden}.gb_J .gb_B,.gb_ka .gb_J .gb_B{background-position:-64px -29px}.gb_1 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_md:not(.gb_nd) .gb_J{display:none;visibility:hidden}}.gb_Q{display:none}.gb_ad{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_ad.gb_bd{color:#3c4043}.gb_Fa.gb_cc .gb_ad{margin-bottom:0}.gb_td.gb_vd .gb_ad{padding-left:4px}.gb_Fa.gb_cc .gb_wd{position:relative;top:-2px}.gb_cd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Fa.gb_Tc{min-width:120px}.gb_Fa.gb_xd .gb_yd{display:none}.gb_Fa.gb_xd .gb_md{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Ed{position:fixed;top:0;width:100%}.gb_zd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Fd{height:64px}.gb_md{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_cc) .gb_md{padding:8px}.gb_Fa.gb_Hd .gb_md{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa .gb_md.gb_nd.gb_Id{min-width:0}.gb_Fa.gb_cc .gb_md{padding:4px;padding-left:8px;min-width:0}.gb_yd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Bd>.gb_yd{display:table-cell;width:100%}.gb_td{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa.gb_cc .gb_td{padding-right:14px}.gb_Cd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Cd>:only-child{display:inline-block}.gb_Dd.gb_4c{padding-left:4px}.gb_Dd.gb_Jd,.gb_Fa.gb_Hd .gb_Dd,.gb_Fa.gb_cc:not(.gb_Kd) .gb_Dd{padding-left:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd{padding-right:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd .gb_Wa{margin-left:10px}.gb_4c{display:inline}.gb_Fa.gb_Xc .gb_Dd.gb_Ld,.gb_Fa.gb_Kd .gb_Dd.gb_Ld{padding-left:2px}.gb_ad{display:inline-block}.gb_Dd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Kd{height:48px}.gb_Fa.gb_Kd{min-width:auto}.gb_Kd .gb_Dd{float:right;padding-left:32px}.gb_Kd .gb_Dd.gb_Md{padding-left:0}.gb_Nd{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_qd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Od{color:black}.gb_Mc{color:white}.gb_Fa a,.gb_Qc a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_Qc svg,.gb_td .gb_ud,.gb_3c .gb_ud{color:#5f6368;opacity:1}.gb_Mc svg,.gb_Qc.gb_Vc svg,.gb_Mc .gb_td .gb_ud,.gb_Mc .gb_td .gb_Lc,.gb_Mc .gb_td .gb_wd,.gb_Qc.gb_Vc .gb_ud{color:rgba(255,255,255,.87)}.gb_Mc .gb_td .gb_Pd:not(.gb_Qd){opacity:.87}.gb_bd{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Mc .gb_bd,.gb_Od .gb_bd{opacity:1}.gb_Rd{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_Mc a.gb_X,.gb_Mc span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_rd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Kd .gb_rd{margin-left:8px}#gb a.gb_Ua.gb_rd{cursor:pointer}.gb_Ua.gb_rd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:focus,.gb_Ua.gb_rd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_rd{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_cc .gb_rd{padding:9px 15px;min-width:80px}.gb_Sd{text-align:left}#gb .gb_Mc a.gb_rd:not(.gb_H),#gb.gb_Mc a.gb_rd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_H.gb_rd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Mc a.gb_rd:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_H.gb_rd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Mc a.gb_rd:focus:not(.gb_H),#gb .gb_Mc a.gb_rd:focus:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_H.gb_rd:focus,#gb a.gb_Ua.gb_H.gb_rd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Mc a.gb_rd:active:not(.gb_H),#gb.gb_Mc a.gb_rd:active{background:#ecf3fe}#gb a.gb_Ua.gb_H.gb_rd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_md .gb_J{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_H .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_H:focus-visible,.gb_Wa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_H:active,.gb_Wa.gb_Uc.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_H .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Jc{vertical-align:middle}.gb_Fa:not(.gb_cc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_Td{max-height:32px;width:78px}.gb_Wa.gb_H .gb_Td{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_eb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_eb.gb_P{height:30px;width:30px}.gb_eb.gb_P:hover,.gb_eb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_fb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_wc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_gb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_gb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_hb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_hb{width:auto}.gb_hb:hover,.gb_hb:focus{opacity:.85}.gb_hd .gb_hb,.gb_hd .gb_Vd{line-height:26px}#gb#gb.gb_hd a.gb_hb,.gb_hd .gb_Vd{font-size:11px;height:auto}.gb_ib{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_ib{opacity:.85}.gb_Wa>.gb_z{padding:3px 3px 3px 4px}.gb_Wd.gb_od{color:#fff}.gb_1 .gb_hb,.gb_1 .gb_ib{opacity:1}#gb#gb.gb_1.gb_1 a.gb_hb,#gb#gb .gb_1.gb_1 a.gb_hb{color:#fff}.gb_1.gb_1 .gb_ib{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Xd .gb_z,.gb_Zd .gb_z{position:absolute;right:1px}.gb_z.gb_0,.gb_jb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_0d.gb_1d .gb_hb{width:30px!important}.gb_2d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_3d .gb_2d,.gb_4d .gb_2d{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.mMopREgTAX8.2019.O","co.in","en","425",0,[4,2,"","","","760405531","0"],null,"OoYsaKPENJqrp84P5f3UkQo",null,0,"og.qtm.yeaJaMsOWhU.L.W.O","AA2YrTuCiUT6mMOHqZDGi6Oyao0tPxem2g","AA2YrTsrW9RjvXXXwuCabDkppBAFz1GXlw","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","nimilibala@gmail.com","","AE0209ETSZ_8YjNEMVt9_4-aHIW5-652-FeaLsjdIofHnJlOEsF-RWTDU6yCxRTtuFO6lTK_hizCT8U_3bbkc_1_lqWTOKtmOw",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.F939Du45chc.O/d=1/rs=AHpOoo8uI5v7Xlp-b-Z4Th_hAAVtm2lZOw/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250407.0_p1","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en","760405531.0",8,null,1,0,null,null,null,null,"",null,null,null,"OoYsaKPENJqrp84P5f3UkQo",0,0,0,null,2,5,"nn",89,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.mMopREgTAX8.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTuCiUT6mMOHqZDGi6Oyao0tPxem2g"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.yeaJaMsOWhU.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTsrW9RjvXXXwuCabDkppBAFz1GXlw"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026bac=1\u0026amb=1\u0026gdafe=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",1,1],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/\u0026timeStmp=1747748410\u0026secTok=.AG5fkS_SMWmXb4KtmKXaX92KVv3w2qHzyQ\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,1,null,0,null,0,0,"8559284470",0],0,null,null,null,1,0,""],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Ga,Ha,cb,eb,jb,fb,$a,lb,pb,Cb,Db,Eb,Fb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Pj=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Da=function(a){if(4&a)return 512&a?512:1024&a?1024:0};_.Fa=function(a,b){return b===void 0?a.j!==Ea&&!!(2&(a.ha[_.v]|0)):!!(2&b)&&a.j!==Ea};Ga=function(a){return a};Ha=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ia=function(a){a=Error(a);Ha(a,"warning");return a};_.Ka=function(a,b){if(a!=null){var c;var d=(c=Ja)!=null?c:Ja={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ha(a,"incident"),_.ka(a))}};
_.Ma=function(a){if(typeof a!=="boolean")throw Error("r`"+_.La(a)+"`"+a);return a};_.Na=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Pa=function(a){if(!(0,_.Oa)(a))throw _.Ia("enum");return a|0};_.Qa=function(a){return a==null?a:(0,_.Oa)(a)?a|0:void 0};_.Ra=function(a){if(typeof a!=="number")throw _.Ia("int32");if(!(0,_.Oa)(a))throw _.Ia("int32");return a|0};_.Sa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};
_.Ta=function(a){return a==null||typeof a==="string"?a:void 0};_.Wa=function(a,b,c){if(a!=null&&a[_.Ua]===_.Va)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Za=function(a){const b=_.Xa(_.Ya);return b?a[b]:void 0};
cb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Xa(_.Ya),g;!e&&f&&(g=a[f])&&g.qd($a);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=ab)!=null?r:Ga)(g-p,p,a,k)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const E=r-p;var q=void 0;((q=b)!=null?q:b={})[E]=w}else f[r]=w}if(k)for(let w in k){q=k[w];
if(q==null||(q=c(q,d))==null)continue;h=+w;let E;if(m&&!Number.isNaN(h)&&(E=h+p)<g)f[E]=q;else{let K;((K=b)!=null?K:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Xa(_.Ya)&&(a=_.Za(a))&&"function"==typeof _.bb&&a instanceof _.bb&&(f[_.Ya]=a.i());return f};
eb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.db)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:cb(a,b,eb)}if(a!=null&&a[_.Ua]===_.Va)return fb(a);if("function"==typeof _.gb&&a instanceof _.gb)return a.j();return}return a};jb=function(a,b){if(b){ab=b==null||b===Ga||b[hb]!==ib?Ga:b;try{return fb(a)}finally{ab=void 0}}return fb(a)};
fb=function(a){a=a.ha;return cb(a,a[_.v]|0,eb)};$a=function(a,b){b<500||_.Ka(kb,1)};
_.mb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-8380417|(b&1023)<<13)}else{if(!Array.isArray(a))throw Error("s");e=a[_.v]|0;2048&e&&!(2&e)&&lb();if(e&256)throw Error("u");if(e&64)return d!==0||e&2048||(a[_.v]=e|2048),a;if(c&&(e|=128,c!==a[0]))throw Error("v");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("x");for(var h in k)if(f=+h,f<g)c[f+b]=k[h],delete k[h];else break;
e=e&-8380417|(g&1023)<<13;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("y");e=e&-8380417|(h&1023)<<13}}}e|=64;d===0&&(e|=2048);a[_.v]=e;return a};lb=function(){_.Ka(nb,5)};
pb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.ob(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Ua]===_.Va){b=a.ha;const d=b[_.v]|0;_.Fa(a,d)?c=a:c=_.ob(b,d);return c}if("function"==typeof _.gb&&a instanceof _.gb)return a};_.ob=function(a,b,c,d){d!=null||(d=!!(34&b));a=cb(a,b,pb,d);d=32;c&&(d|=2);b=b&8380609|d;a[_.v]=b;return a};
_.qb=function(a){const b=a.ha,c=b[_.v]|0;return _.Fa(a,c)?new a.constructor(_.ob(b,c,!1)):a};_.sb=function(a){if(a.j!==Ea)return!1;var b=a.ha;b=_.ob(b,b[_.v]|0);b[_.v]|=2048;a.ha=b;a.j=void 0;a.v=void 0;return!0};_.tb=function(a){if(!_.sb(a)&&_.Fa(a,a.ha[_.v]|0))throw Error();};
_.ub=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>13&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};_.vb=function(a){return!!(2&a)&&!!(4&a)||!!(256&a)};_.xb=function(a,b,c,d,e){a=_.wb(a,d,e,f=>_.Wa(f,c,b));if(a!=null)return a};_.yb=function(a,b){return a=(2&b?a|2:a&-3)&-273};
_.zb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Ab=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Bb=function(a){for(const b in a)return!1;return!0};Cb=Object.defineProperty;
Db=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Eb=Db(this);Fb=function(a,b){if(b)a:{var c=Eb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Cb(c,a,{configurable:!0,writable:!0,value:b})}};Fb("globalThis",function(a){return a||Eb});
Fb("Symbol.dispose",function(a){return a?a:Symbol("b")});Fb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});
Fb("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Hb,Lb;_.Gb=_.Gb||{};_.t=this||self;Hb=_.t._F_toggles||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.La=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Jb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Kb="closure_uid_"+(Math.random()*1E9>>>0);Lb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Lb;return _.z.apply(null,arguments)};
_.Mb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Xa=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Hj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Pb,Nb,Qb,Ob;_.db=_.ba(a=>fa?a>=Nb&&a<=Ob:a[0]==="-"?ja(a,Pb):ja(a,Qb));Pb=Number.MIN_SAFE_INTEGER.toString();Nb=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Qb=Number.MAX_SAFE_INTEGER.toString();Ob=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Rb=typeof TextDecoder!=="undefined";_.Sb=typeof TextEncoder!=="undefined";var Tb=!!(Hb[0]>>15&1);var Ub;if(Hb[0]>>14&1)Ub=Tb;else{var Vb=_.Ib("WIZ_global_data.oxN3nb"),Wb=Vb&&Vb[610401301];Ub=Wb!=null?Wb:!1}var na=Ub;var oa,Xb=_.t.navigator;oa=Xb?Xb.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.Yb=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.Zb=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.$b=function(a){_.$b[" "](a);return a};_.$b[" "]=function(){};var nc;_.ac=_.ra();_.bc=_.sa();_.cc=_.u("Edge");_.dc=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.ec=_.ma()&&!_.u("Edge");_.fc=_.za();_.hc=wa()?oa.platform==="Windows":_.u("Windows");_.ic=wa()?oa.platform==="Android":_.u("Android");_.jc=xa();_.kc=_.u("iPad");_.lc=_.u("iPod");_.mc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.dc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.cc)return/Edge\/([\d\.]+)/.exec(c);if(_.bc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.ec)return/WebKit\/(\S+)/.exec(c);if(_.ac)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.bc){var oc;const c=_.t.document;oc=c?c.documentMode:void 0;if(oc!=null&&oc>parseFloat(a)){nc=String(oc);break a}}nc=a}_.pc=nc;_.qc=_.ta();_.rc=xa()||_.u("iPod");_.sc=_.u("iPad");_.tc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.uc=ua();_.vc=_.va()&&!_.ya();var kb,nb,hb;_.Ya=_.Ca();_.wc=_.Ca();kb=_.Ca();_.xc=_.Ca();nb=_.Ca();_.Ua=_.Ca("m_m",!0);hb=_.Ca();_.yc=_.Ca();var Ac;_.v=_.Ca("jas",!0);Ac=[];Ac[_.v]=7;_.zc=Object.freeze(Ac);var Ea;_.Va={};Ea={};_.Bc=Object.freeze({});var ib={};var Ja=void 0;_.Cc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Dc=Number.isSafeInteger;_.Oa=Number.isFinite;_.Ec=Math.trunc;var ab;_.Fc=_.ia(0);_.Gc={};_.Hc=function(a,b,c,d,e){b=_.wb(a.ha,b,c,e);if(b!==null||d&&a.v!==Ea)return b};_.wb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Ic=function(a,b,c,d){_.tb(a);const e=a.ha;_.ub(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.ha,f=e[_.v]|0;b=_.xb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Fa(a,f)){const g=_.qb(b);g!==b&&(_.sb(a)&&(e=a.ha,f=e[_.v]|0),b=g,_.ub(e,f,c,b,d))}return b};_.D=function(a,b,c){c==null&&(c=void 0);_.Ic(a,b,c);return a};_.Jc=function(a,b,c,d){return _.Qa(_.Hc(a,b,c,d))};_.F=function(a,b,c=!1,d){let e;return(e=_.Na(_.Hc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Ta(_.Hc(a,b,d)))!=null?e:c};_.H=function(a,b,c){return _.Ta(_.Hc(a,b,c,_.Gc))};
_.J=function(a,b,c,d){return _.Ic(a,b,c==null?c:_.Ma(c),d)};_.L=function(a,b,c){return _.Ic(a,b,c==null?c:_.Ra(c))};_.M=function(a,b,c,d){return _.Ic(a,b,_.Sa(c),d)};_.N=function(a,b,c,d){return _.Ic(a,b,c==null?c:_.Pa(c),d)};_.O=class{constructor(a,b,c){this.ha=_.mb(a,b,c)}toJSON(){return jb(this)}va(a){return JSON.stringify(jb(this,a))}};_.O.prototype[_.Ua]=_.Va;_.O.prototype.toString=function(){return this.ha.toString()};_.Kc=_.zb();_.Lc=_.zb();_.Mc=_.zb();_.Oc=Symbol();var Pc=class extends _.O{constructor(a){super(a)}};_.Qc=class extends _.O{constructor(a){super(a)}D(a){return _.L(this,3,a)}};var Rc=class extends _.O{constructor(a){super(a)}Hc(a){return _.M(this,24,a)}};_.Sc=class extends _.O{constructor(a){super(a)}};_.Q=function(){this.qa=this.qa;this.Y=this.Y};_.Q.prototype.qa=!1;_.Q.prototype.isDisposed=function(){return this.qa};_.Q.prototype.dispose=function(){this.qa||(this.qa=!0,this.P())};_.Q.prototype[Symbol.dispose]=function(){this.dispose()};_.Q.prototype.P=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Tc=class extends _.Q{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}ob(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].ob(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Vc=class extends _.Q{constructor(){var a=_.Uc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Wc=class extends _.O{constructor(a){super(a)}};var Xc=class extends _.O{constructor(a){super(a)}};var $c;_.Yc=function(a,b,c=98,d=new _.Qc){if(a.i){const e=new Pc;_.M(e,1,b.message);_.M(e,2,b.stack);_.L(e,3,b.lineNumber);_.N(e,5,1);_.D(d,40,e);a.i.log(c,d)}};$c=class{constructor(){var a=Zc;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Qc){_.Yc(this,a,98,c)}};var ad,bd;ad=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.Yb(c,b,a)}catch(d){console.error(d)}}}};_.cd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new bd(a,b,c));ad(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("C");this.i=a;ad(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("C");this.j=a;ad(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
bd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.dd=a=>{var b="lc";if(a.lc&&a.hasOwnProperty(b))return a.lc;b=new a;return a.lc=b};_.ed=class{constructor(){this.v=new _.cd;this.i=new _.cd;this.D=new _.cd;this.B=new _.cd;this.C=new _.cd;this.A=new _.cd;this.o=new _.cd;this.j=new _.cd;this.F=new _.cd}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.dd(_.ed)}};var id;_.gd=function(){return _.C(_.fd,Rc,1)};_.hd=function(){return _.C(_.fd,_.Sc,5)};id=class extends _.O{constructor(a){super(a)}};var jd;window.gbar_&&window.gbar_.CONFIG?jd=window.gbar_.CONFIG[0]||{}:jd=[];_.fd=new id(jd);var Zc=_.C(_.fd,Xc,3)||new Xc;_.gd()||new Rc;_.Uc=new $c;_.A("gbar_._DumpException",function(a){_.Uc?_.Uc.log(a):console.error(a)});_.kd=new Vc;var md;_.nd=function(a,b){var c=_.ld.i();if(a in c.i){if(c.i[a]!=b)throw new md;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Bb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.ld=class{constructor(){this.i={};this.j={}}static i(){return _.dd(_.ld)}};_.od=class extends _.aa{constructor(){super()}};md=class extends _.od{};_.A("gbar.A",_.cd);_.cd.prototype.aa=_.cd.prototype.then;_.A("gbar.B",_.ed);_.ed.prototype.ba=_.ed.prototype.M;_.ed.prototype.bb=_.ed.prototype.N;_.ed.prototype.bd=_.ed.prototype.qa;_.ed.prototype.bf=_.ed.prototype.Y;_.ed.prototype.bg=_.ed.prototype.L;_.ed.prototype.bh=_.ed.prototype.K;_.ed.prototype.bj=_.ed.prototype.J;_.ed.prototype.bk=_.ed.prototype.G;_.A("gbar.a",_.ed.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var pd=new Tc;_.nd("api",pd);
var qd=_.hd()||new _.Sc,rd=window,sd=_.y(_.H(qd,8));rd.__PVT=sd;_.nd("eq",_.kd);
}catch(e){_._DumpException(e)}
try{
_.td=class extends _.O{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var ud=class extends _.O{constructor(a){super(a)}};var vd=class extends _.Q{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.H(a,1));_.Na(_.Hc(a,12))!=null&&(d.dpo=_.x(_.F(a,12)));d.ms=_.y(_.H(a,2));d.m=_.y(_.H(a,3));d.l=[];_.G(b,1)&&(a=_.H(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.H(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var wd=_.C(_.fd,_.Wc,14);if(wd){var xd=_.C(_.fd,_.td,9)||new _.td,yd=new ud,Ad=new vd;Ad.init(wd,xd,yd);_.nd("gs",Ad)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_nimilibala@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./APP.py - Colab_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250514-060044_RC00_758624382'; var colabScsVersion = 'a9ced4aed8e2fce0c836e00ae7f77be7'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_nvidia_cudf_facts_to_chat_context\x22: true, \x22add_prompt_cell\x22: false, \x22agent_scroll_delay_ms\x22: 200, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22bigquery_sql_engine\x22: false, \x22bigquery_sql_engine_library\x22: \x22\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: true, \x22cell_ui_refresh\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22cloud_run\x22: false, \x22code_report_millis\x22: 600000, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: false, \x22composer_auto_code\x22: false, \x22composer_context_max_variable_length\x22: 500000, \x22composer_debug_info\x22: false, \x22composer_entrypoint_explain_cell\x22: false, \x22composer_entrypoint_explain_error\x22: false, \x22composer_entrypoint_gemini_spark\x22: false, \x22composer_fp_ai_demo\x22: false, \x22composer_on_empty\x22: true, \x22composer_resize_notebook_footer\x22: true, \x22composer_static_content\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: false, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22dsa_sample_datasets_toast\x22: true, \x22embedded_toolbar_customization\x22: false, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_completions_backend_switching\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_edu_subscription_ui\x22: false, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: true, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22i18n_runtime_labels\x22: true, \x22import_data\x22: false, \x22import_gemini_api_key\x22: true, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22interactive_sheet_next_steps\x22: true, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: false, \x22kaggle_submit_to_competition\x22: false, \x22kernel_use_connected_endpoint_for_unassign\x22: true, \x22key_promoter\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: false, \x22multi_modal_context_for_transform\x22: false, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prepare_runtime_for_notebook\x22: false, \x22prereq_cells_next_steps\x22: true, \x22presentation_mode\x22: false, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kws\x22: true, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: false, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22signup_ccu_increase\x22: true, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.32_60\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22sql_completion_lsp\x22: false, \x22status_bar_ui_refresh\x22: true, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22suggest_plots\x22: true, \x22task_service_max_poll_count\x22: 180, \x22task_service_poll_interval_ms\x22: 500, \x22task_service_wait_before_polling_ms\x22: 1000, \x22term4all\x22: false, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22toolbar_run_button\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: true, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22trim_filename_extension\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22updated_inline_cell_diff\x22: true, \x22use_corplogin\x22: true, \x22use_tpu_eligibility_lists\x22: true, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V28\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730393, 20730363, 20730420, 20730265, 20730324, 20730315, 20730369, 20730414, 20730150, 20730177, 20730183, 20730375\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_nvidia_cudf_facts_to_chat_context\x22: 45685179, \x22add_prompt_cell\x22: 45644995, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allowed_public_url_domains\x22: 45425558, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22bigquery_sql_engine\x22: 45697421, \x22bigquery_sql_engine_library\x22: 45700104, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22cloud_run\x22: 45697172, \x22code_report_millis\x22: 45658073, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_debug_info\x22: 45688718, \x22composer_entrypoint_explain_cell\x22: 45693388, \x22composer_entrypoint_explain_error\x22: 45692068, \x22composer_entrypoint_gemini_spark\x22: 45691834, \x22composer_fp_ai_demo\x22: 45697025, \x22composer_on_empty\x22: 45690576, \x22composer_resize_notebook_footer\x22: 45696289, \x22composer_static_content\x22: 45697502, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22dsa_sample_datasets_toast\x22: 45682045, \x22embedded_toolbar_customization\x22: 45692827, \x22embedded_use_websockets\x22: 45691694, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_completions_backend_switching\x22: 45662651, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_edu_subscription_ui\x22: 45693272, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22i18n_runtime_labels\x22: 45662916, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22interactive_sheet_next_steps\x22: 45634324, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22kaggle_submit_to_competition\x22: 45693906, \x22kernel_use_connected_endpoint_for_unassign\x22: 45684913, \x22key_promoter\x22: 45425570, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22multi_modal_context_for_transform\x22: 45687634, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prepare_runtime_for_notebook\x22: 45699118, \x22prereq_cells_next_steps\x22: 45640400, \x22presentation_mode\x22: 45699417, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kws\x22: 45650184, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22signup_ccu_increase\x22: 45689970, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22sql_completion_lsp\x22: 45688254, \x22status_bar_ui_refresh\x22: 45685043, \x22suggest_plots\x22: 45696393, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22toolbar_run_button\x22: 45697404, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22trim_filename_extension\x22: 45691676, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22updated_inline_cell_diff\x22: 45667103, \x22use_corplogin\x22: 45425606, \x22use_tpu_eligibility_lists\x22: 45682573, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'nimilibala@gmail.com'; var colabRenderDataToken = 'AFWLbD2Cjk-S2VGqrtgUsdBvheB8Zq5acChjN8nNhLfhgInz0ByABSlzDNOH1CMkd3BTamOfJToJTv9aa5i2IebfpnJXHPJ3k4vk'; var colabConfig = '\x5b\x5b\x22nimilibala@gmail.com\x22,\x5b1,\x22AHXL0D3GWHe2JDz0bSCLIk3aQv+72HW4AgUVJnjTwz4d8vyCbD0C8pnDcguMcReqB+TrzBUI6wTU7FejajqLaMDRv39Ybj7oyG5REevxnBHqdGrPA00rds6QUOofaSzz7zlb7Eh6ROuydi\/mPrZiMIgUKHOQCG+77Qhf8Ya+Er\/DcrLrd7TArr2b\/hRHwEP43dt7KAbbXbn3Xw27PZpxbBERswMSrFfbff0CCVxpFTdJJI5sDY7RPbb4NnIxeI7yywHVZZq0+Bi9myXdpjZuGInopiYUmIr+jaT+aZIm\/yjinZwRyLkEvqhOEKtk7QmBa81ywcOmxngFomXq7AMBY1y7z9N0l4yX1Kdjxas2ohCQa\/+AtSUqefi6z6LZv640cvc67StS65duiDQpK2wykFCmMwJjOmZ2hCJAx4k1BkoAap\/RSmE2M5tYY0VLMCXrkWLyHJcT5+glsvRsS+QZQqrFwKrRAGx55puSly\/QC4qpoeGxqdxnlGAgjd0pklFHc4B2AEMEmCNs8DK9pAzzJPpXc7y0YzKF08K9xGM1RBW0xj3nPvVDDf4J3HDwVskFRaHYMF52PX+TuNp3scBwee4B\/3emnU8zwpCrpPhfWdH0XLSh5kZiIYFvR2I7Ts4HQnuxgdGasWaLWK4CIaDaB0WQaOWXHUosC1KV3hCbwVDrQheMhMqTUlI8200WcnwcmAmc64HcEty5YrrLodw4Mct5\/BLT\/\/PL16Wve64HTMS3Lw5PTYZ3flMKu\/MjNKDWn\/w7\/EKVc5c1vQtXmRZWOleeGhCEQfzFzfnkZDFzH3xYrGI7hbbw\/Ael9020nUxZ14ffP38ZkzKl8OB305CfOjIFr0Ar4Ne1hLMryIDL+DGza\/K+9SYfWHzp8atQTCn7QwTW5UtraAXwUv5BRExKZlXBYom\/TtpKl67CDuYJbIo7IdiooPyA4HfWODBordxjvJvVG7UcjUwWsbXWRzTnQL26bqPWEM1boOk0cIV3iXOrEF+u3gY8PIidjhW9oVT\/rmDVQbyiIZig661oduhNt\/Zn0aOSPBNwO5\/i0LkLcFG3JZi9K1eIrgWPM9Q4XVVKlH8caTQw5JHwwe6FyOkLvOfiYWSykdzduiGie8duSOq8ygCt1AkPQsdXmPKa1EoYtq2F6DnGhScrGC3Vlv4n8NMd3dFg\/k1Qk2VOv1kaAONRpmKc4Gi5Wk3VFrUU\/c2xClDLkarwSmIUY3xu3ICvZQkKPN1aCizMTk5+Gm0Os7WWqkrGhaXnbQHct30Y1ZTHpoBcw3VU8mzh4Dx10TTmOzQd+mtwC5Yrq2WVrC\/BDLcX1HAcu9VIoP\/DwMkoDnaSBgdiAeLTpyfu9tgwju+aEz9BfLlxfEjUL0hgiiQ4SCq+Q6bvN4ZWAYqN9urCtzC2irDv9G8hTVm4B7gErewVsz5+UMBz\/99Od\/W9COAUf3HIu0tI6ofJ+jhtEJa0HqBm3vAsuEe7qQhpGiI\/UolDVUlSzmc+phFJZe+JHInS8Fkiq7JSrpgKV\/QWOWHiybc6hJErvCnHUeMTAaAqSow07CCrxohk7EsVzpLdcpAFgPZwFUPqahfBdS1meYVezK4\/v+jFqxKjoChd0dRxrt7yT7oG1njTMPXAZmjHyDLvaMHqq\/2JqJYGR+MJNZFNTiEu8R9\/6iilOIN2Qr9x4o30Ws49cuymP04gZftgNu6uHD2OsWgJPox4x3cZqU76fcYgXU7ryJGAu1d+RdqBAtZS7KnOpKi+TJspyl5XV0O6jrqsWY+NHKneKnD9WlVhLVEMs3Dqw6qy8Jg0+m\/FB8wsCuF5rIuW3l+dCRfE3yGHNkhoDCrTdiEhmTBZGUyVmUslsXx74dxLSuWUE\/11zP6vssavxVXikwvcZv2PapgtFyK+i6w0KE7Boug\x3d\x22,\x22AJ9oCCx+E5I1ibMlRPpA9MwFxHREattxYciObeJecsFm4roPuDZ7o9OrvkcrsFk4f4Bih4mycA\/F1EOMynE\/vltMVxFgXfGqrFzcMi1lz1pd+z1Xda7pLE9WqRycaqNiu4edVSJ3u1Z5\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22,0,0,0\x5d,\x5b1,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/a9ced4aed8e2fce0c836e00ae7f77be7/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./APP.py - Colab_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./APP.py - Colab_files/rs=AA2YrTuCiUT6mMOHqZDGi6Oyao0tPxem2g" nonce=""></script><link type="text/css" href="./APP.py - Colab_files/rs=AA2YrTsrW9RjvXXXwuCabDkppBAFz1GXlw" rel="stylesheet"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./APP.py - Colab_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./APP.py - Colab_files/editor.main.css"><script async="async" type="text/javascript" src="./APP.py - Colab_files/editor.main.nls.js.download"></script><script src="./APP.py - Colab_files/api.js.download" nonce=""></script><script src="./APP.py - Colab_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: #234521;
--vscode-diffEditor-removedTextBackground: #5b2022;
--vscode-diffEditor-insertedLineBackground: #22331f;
--vscode-diffEditor-removedLineBackground: #3c1a1a;
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #82b76c; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #69a5d7; }
.mtk11 { color: #f28b82; }
.mtk12 { color: #d7ba7d; }
.mtk13 { color: #d49d87; }
.mtk14 { color: #dcdcdc; }
.mtk15 { color: #808080; }
.mtk16 { color: #4ec9b0; }
.mtk17 { color: #dcdcaa; }
.mtk18 { color: #f44747; }
.mtk19 { color: #82c6ff; }
.mtk20 { color: #c99cc6; }
.mtk21 { color: #c586c0; }
.mtk22 { color: #a79873; }
.mtk23 { color: #dd6a6f; }
.mtk24 { color: #5bb498; }
.mtk25 { color: #909090; }
.mtk26 { color: #778899; }
.mtk27 { color: #ff00ff; }
.mtk28 { color: #b46695; }
.mtk29 { color: #ff0000; }
.mtk30 { color: #4f76ac; }
.mtk31 { color: #3dc9b0; }
.mtk32 { color: #74b0df; }
.mtk33 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><script async="async" type="text/javascript" src="./APP.py - Colab_files/python.js.download"></script></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./APP.py - Colab_files/gapi_loader.js.download" nonce=""></script><script src="./APP.py - Colab_files/socketio_binary.js.download" nonce=""></script><script src="./APP.py - Colab_files/analytics_binary.js.download" nonce=""></script><script src="./APP.py - Colab_files/MathJax.js.download" nonce=""></script><script src="./APP.py - Colab_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./APP.py - Colab_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$641307570$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$641307570$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$641307570$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$641307570$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Loading...</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_S" ng-non-bindable=""><div class="gb_Bc"><div>Google Account</div><div class="gb_g">PRIYADHARSHINI _NITT</div><div>nimilibala@gmail.com</div><div class="gb_Cc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Fd;Fd=class extends _.od{};_.Gd=function(a,b){if(b in a.i)return a.i[b];throw new Fd;};_.Hd=function(a){return _.Gd(_.ld.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Kd;_.Id=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Kd=function(a){return new _.Jd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Ld=globalThis.trustedTypes;_.Md=class{constructor(a){this.i=a}toString(){return this.i}};_.Nd=new _.Md("about:invalid#zClosurez");_.Jd=class{constructor(a){this.wh=a}};_.Od=[Kd("data"),Kd("http"),Kd("https"),Kd("mailto"),Kd("ftp"),new _.Jd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Pd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Qd=new _.Pd(_.Ld?_.Ld.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Ud,fe,Td,Vd,$d;_.Rd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Oa)(a)?a|0:void 0};_.Sd=function(a,b){return a.lastIndexOf(b,0)==0};Ud=function(){let a=null;if(!Td)return a;try{const b=c=>c;a=Td.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Wd=function(){Vd===void 0&&(Vd=Ud());return Vd};_.Yd=function(a){const b=_.Wd();a=b?b.createScriptURL(a):a;return new _.Xd(a)};
_.Zd=function(a){if(a instanceof _.Xd)return a.i;throw Error("E");};_.ae=function(a){if($d.test(a))return a};_.be=function(a){if(a instanceof _.Md)if(a instanceof _.Md)a=a.i;else throw Error("E");else a=_.ae(a);return a};_.ce=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.R=function(a,b,c){return _.Na(_.Hc(a,b,c,_.Gc))};_.de=function(a,b){return _.Rd(_.Hc(a,b,void 0,_.Gc))};
_.ee=function(a){var b=_.La(a);return b=="array"||b=="object"&&typeof a.length=="number"};Td=_.Ld;_.Xd=class{constructor(a){this.i=a}toString(){return this.i+""}};$d=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var ke,oe,ge;_.ie=function(a){return a?new ge(_.he(a)):fe||(fe=new ge)};_.je=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.S=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a?a=(b||c).querySelector(a?"."+a:""):(b=b||c,a=(a?b.querySelectorAll(a?"."+a:""):b.getElementsByTagName("*"))[0]||null));return a||null};
_.le=function(a,b){_.Ab(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:ke.hasOwnProperty(d)?a.setAttribute(ke[d],c):_.Sd(d,"aria-")||_.Sd(d,"data-")?a.setAttribute(d,c):a[d]=c})};ke={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.me=function(a){return a?a.defaultView:window};_.pe=function(a,b){const c=b[1],d=_.ne(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.le(d,c));b.length>2&&oe(a,d,b);return d};oe=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.ee(f)||_.Jb(f)&&f.nodeType>0?d(f):_.Yb(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Id(f):f,d)}};
_.qe=function(a){return _.ne(document,a)};_.ne=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.re=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.se=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.te=function(a,b){return a&&b?a==b||a.contains(b):!1};_.he=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};ge=function(a){this.i=a||_.t.document||document};_.n=ge.prototype;
_.n.H=function(a){return _.je(this.i,a)};_.n.Ua=function(a,b,c){return _.pe(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.xe=_.re;_.n.Sf=_.se;_.n.Rf=_.te;
}catch(e){_._DumpException(e)}
try{
_.Fi=function(a){const b=_.ce("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Gi=function(a){if(!a)return null;a=_.H(a,4);var b;a===null||a===void 0?b=null:b=_.Yd(a);return b};_.Hi=function(a,b,c){a=a.ha;return _.xb(a,a[_.v]|0,b,c)!==void 0};_.Ii=class extends _.O{constructor(a){super(a)}};_.Ji=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Li=function(a,b,c){a<b?Ki(a+1,b):_.Uc.log(Error("ca`"+a+"`"+b),{url:c})},Ki=function(a,b){if(Mi){const c=_.qe("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.Zd(Mi);_.Fi(c);c.onerror=_.Mb(Li,a,b,c.src);_.Ji("HEAD")[0].appendChild(c)}},Ni=class extends _.O{constructor(a){super(a)}};var Oi=_.C(_.fd,Ni,17)||new Ni,Pi,Mi=(Pi=_.C(Oi,_.Ii,1))?_.Gi(Pi):null,Qi,Ri=(Qi=_.C(Oi,_.Ii,2))?_.Gi(Qi):null,Si=function(){Ki(1,2);if(Ri){const a=_.qe("LINK");a.setAttribute("type","text/css");a.href=_.Zd(Ri).toString();a.rel="stylesheet";let b=_.ce("style",document);b&&a.setAttribute("nonce",b);_.Ji("HEAD")[0].appendChild(a)}};(function(){const a=_.gd();if(_.R(a,18))Si();else{const b=_.de(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Si,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./APP.py - Colab_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$641307570$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><a id="link" class="button" href="https://colab.research.google.com/drive/1PCga96CMC_NQg61iq2IiLVF7R0IXtb7w#notebook-main"><!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </a>
    </template><!--?lit$641307570$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$641307570$-->
    <!--?lit$641307570$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning" hidden=""><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$641307570$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1PCga96CMC_NQg61iq2IiLVF7R0IXtb7w#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$641307570$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><div id="header-logo">
              <!--?lit$641307570$--> <!--?lit$641307570$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$641307570$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$641307570$--> <!--?lit$641307570$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 73.5px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events></input><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">APP.pyS_</colab-input-sizer>
            <!--?lit$641307570$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$641307570$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-text-button id="button" class=" save-message " value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->sync</md-icon><!--?lit$641307570$-->Saving...</md-text-button><!--?lit$641307570$--><!--?--></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$641307570$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$641307570$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$641307570$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$641307570$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$641307570$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$641307570$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$641307570$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$641307570$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$641307570$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$641307570$-->
      <!--?lit$641307570$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$641307570$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$641307570$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$641307570$--> <md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->people</md-icon>
                <!--?lit$641307570$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$641307570$--> <md-text-button class="show-chat-button" id="show-chat-button" command="show-chat" data-aria-label="Show Gemini" aria-describedby="show-chat-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Show Gemini">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$641307570$-->Gemini
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Show Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Fa gb_Kd gb_3d gb_Xc" id="gb"><div class="gb_Dd gb_0d gb_yd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Re" style="display:block"><div class="gb_4c"></div><div class="gb_z gb_dd gb_Nf gb_0"><div class="gb_D gb_jb gb_Nf gb_0"><a class="gb_B gb_Za gb_0" aria-expanded="false" aria-label="Google Account: PRIYADHARSHINI _NITT  
(nimilibala@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_P gbii" src="./APP.py - Colab_files/unnamed.png" srcset="https://lh3.google.com/u/0/ogw/AF2bZyjtFTTE4_hAe49nAhggw7CRK8sn-gdtzs-62llYQ1nKtg=s32-c-mo 1x, https://lh3.google.com/u/0/ogw/AF2bZyjtFTTE4_hAe49nAhggw7CRK8sn-gdtzs-62llYQ1nKtg=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""><div class="gb_Q gb_R" aria-hidden="true"><svg class="gb_Ka" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_La" cx="7" cy="7" r="7"></circle><path class="gb_Na" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Bd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.Bd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("A`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Cd=document.querySelector(".gb_J .gb_B"),Dd=document.querySelector("#gb.gb_Tc");Cd&&!Dd&&_.Bd(_.kd,Cd,"click");
}catch(e){_._DumpException(e)}
try{
_.gh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].fa()&&a.i[b].B())return a.i[b];return null};_.hh=function(a,b){a.i[b.J()]=b};var ih=new class extends _.Q{constructor(){var a=_.Uc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.gh(this)&&_.gh(this).J()==a||this.i[a].R(!0))}Pa(a){this.j=a;for(const b in this.i)this.i[b].fa()&&this.i[b].Pa(a)}fc(a){return a in this.i?this.i[a]:null}};_.nd("dd",ih);
}catch(e){_._DumpException(e)}
try{
_.yi=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Ai=document.querySelector(".gb_z .gb_B"),Bi=document.querySelector("#gb.gb_Tc");Ai&&!Bi&&_.Bd(_.kd,Ai,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$641307570$-->
    <!--?lit$641307570$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
        <!--?lit$641307570$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$641307570$--><span class="screenreader-only"><!--?lit$641307570$-->Show command palette <!--?lit$641307570$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$641307570$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$641307570$-->Commands
          </colab-toolbar-button>
          <span class="colab-separator"></span>
    <!--?lit$641307570$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
        <!--?lit$641307570$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$641307570$--><span class="screenreader-only"><!--?lit$641307570$-->Insert code cell below <!--?lit$641307570$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$641307570$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$641307570$-->Code
          </colab-toolbar-button>
          <!--?lit$641307570$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
        <!--?lit$641307570$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$641307570$--><span class="screenreader-only"><!--?lit$641307570$-->Add text cell <!--?lit$641307570$--></span>
      </md-text-button>
      <!--?lit$641307570$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$641307570$-->Text
          </colab-toolbar-button>
        
    <!--?lit$641307570$-->
    <!--?lit$641307570$-->
    <!--?lit$641307570$-->
    <!--?lit$641307570$-->
    <!--?lit$641307570$-->
    <!--?lit$641307570$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-text-button id="button" class=" save-message " value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->sync</md-icon><!--?lit$641307570$-->Saving...</md-text-button><!--?lit$641307570$--><!--?--></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>

    <!--?lit$641307570$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$641307570$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$641307570$--><!--?lit$641307570$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$641307570$--> <!--?lit$641307570$--><md-icon-button id="connect-icon" class="icon-okay" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connected to
Python 3 Google Compute Engine backend
RAM: 1.60 GB/12.67 GB
Disk: 37.35 GB/107.72 GB"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
        <!--?lit$641307570$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$641307570$--><span class="screenreader-only"><!--?lit$641307570$-->Connected to
Python 3 Google Compute Engine backend
RAM: 1.60 GB/12.67 GB
Disk: 37.35 GB/107.72 GB <!--?lit$641307570$--></span>
      </md-text-button>
      <!--?lit$641307570$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connected to
Python 3 Google Compute Engine backend
RAM: 1.60 GB/12.67 GB
Disk: 37.35 GB/107.72 GB" shortcut=""><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Connected to</div><!----><!----><div><!--?lit$641307570$-->Python 3 Google Compute Engine backend</div><!----><!----><div><!--?lit$641307570$-->RAM: 1.60 GB/12.67 GB</div><!----><!----><div><!--?lit$641307570$-->Disk: 37.35 GB/107.72 GB</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$641307570$--> <div id="connect-button-resource-display">
        <!--?lit$641307570$--><colab-usage-sparkline class="ram" label="RAM"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$641307570$-->RAM</div>
      <!--?lit$641307570$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
        <!--?lit$641307570$--><colab-usage-sparkline class="disks" label="Disk"><template shadowrootmode="open"><!---->
      <div class="label"><!--?lit$641307570$-->Disk</div>
      <!--?lit$641307570$-->
      <canvas height="14" width="20"></canvas>
    </template></colab-usage-sparkline>
      </div>
      </colab-toolbar-button>
      <!--?lit$641307570$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$641307570$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$641307570$-->
    <span class="collapsed-options">
      <!--?lit$641307570$--><span class="colab-separator"></span>
      <!--?lit$641307570$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$641307570$--> <md-icon-button class="show-chat-button" id="show-chat-button-toolbar" command="show-chat" data-aria-label="Show Gemini" aria-describedby="show-chat-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show Gemini">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button-toolbar" id="show-chat-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Show Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$641307570$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$641307570$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$641307570$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$641307570$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$641307570$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$641307570$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$641307570$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->code</md-icon>
    </md-icon-button> <!--?lit$641307570$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$641307570$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$641307570$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$641307570$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->folder</md-icon>
    </md-icon-button> <!--?lit$641307570$-->
      </div></div>
        <div class="left-pane-bottom"></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$641307570$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$641307570$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-yvNEErYX7IEs" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$641307570$--><div class="indicator"></div>
      </div>
      <!--?lit$641307570$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-yvNEErYX7IEs"><!--?lit$641307570$--><!--?lit$641307570$-->Notebook<!--?--></span>
            <!--?lit$641307570$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$641307570$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$641307570$-->
              <div class="notebook-content ">
                <!--?lit$641307570$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Text
        </md-outlined-button>
        <!--?lit$641307570$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code code-has-output" id="cell-nJCx0PpP7IEU" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$641307570$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$641307570$--><span class="execution-count"><!--?lit$641307570$-->[1]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$641307570$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$641307570$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$641307570$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by PRIYADHARSHINI _NITT
7:11 PM (47 minutes ago)
executed in 23.138s"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$641307570$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$641307570$-->executed by PRIYADHARSHINI _NITT</div><!----><!----><div><!--?lit$641307570$-->7:11 PM (47 minutes ago)</div><!----><!----><div><!--?lit$641307570$-->executed in 23.138s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$641307570$--><div id="status" class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$641307570$-->23s</div>
    </div>
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;google.colab&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;files</span></span><br><span><span class="mtk1">uploaded&nbsp;=&nbsp;files.upload</span><span class="mtk14">()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$641307570$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div class="outputview" style="height: 73px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./APP.py - Colab_files/outputframe.html" class="" style="height: 73px;"></iframe></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Text
        </md-outlined-button>
        <!--?lit$641307570$-->
      </div><hr>
    </div></div><div class="cell code code-has-output" id="cell-X7n2I2vC-SGa" tabindex="-1" role="region" aria-label="Cell 1: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$641307570$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$641307570$--><span class="execution-count"><!--?lit$641307570$-->[3]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$641307570$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$641307570$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$641307570$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by PRIYADHARSHINI _NITT
7:25 PM (33 minutes ago)
executed in 6.831s"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$641307570$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$641307570$-->executed by PRIYADHARSHINI _NITT</div><!----><!----><div><!--?lit$641307570$-->7:25 PM (33 minutes ago)</div><!----><!----><div><!--?lit$641307570$-->executed in 6.831s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$641307570$--><div id="status" class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$641307570$-->6s</div>
    </div>
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk19">!</span><span class="mtk1">pip&nbsp;install&nbsp;streamlit&nbsp;pyngrok&nbsp;--quiet</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$641307570$-->Start coding or <span tabindex="0" role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 1 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-3 output_text"><pre>     <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">44.3/44.3 kB</span><span> </span><span style="color: var(--ansi-red);">2.4 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">9.9/9.9 MB</span><span> </span><span style="color: var(--ansi-red);">52.2 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">6.9/6.9 MB</span><span> </span><span style="color: var(--ansi-red);">47.1 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span>   <span style="color: var(--ansi-bright-black);">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><span> </span><span style="color: var(--ansi-green);">79.1/79.1 kB</span><span> </span><span style="color: var(--ansi-red);">5.2 MB/s</span><span> eta </span><span style="color: var(--ansi-cyan);">0:00:00</span><span>
</span></pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Text
        </md-outlined-button>
        <!--?lit$641307570$-->
      </div><hr>
    </div></div><div class="cell code code-has-output" id="cell-T6CGhIFX9bGO" tabindex="-1" role="region" aria-label="Cell 2: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$641307570$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution hovered">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$641307570$--><span class="execution-count"><!--?lit$641307570$-->[12]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$641307570$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$641307570$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$641307570$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by PRIYADHARSHINI _NITT
8:00 PM (0 minutes ago)
executed in 0.023s"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$641307570$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$641307570$-->executed by PRIYADHARSHINI _NITT</div><!----><!----><div><!--?lit$641307570$-->8:00 PM (0 minutes ago)</div><!----><!----><div><!--?lit$641307570$-->executed in 0.023s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$641307570$--><div id="status" class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$641307570$-->0s</div>
    </div>
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="25" data-mode-id="notebook-python" style="height: 409px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/4" style="width: 1146px; height: 409px;"><div data-mprt="3" class="overflow-guard" style="width: 1146px; height: 409px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 409px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 409px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 409px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1140px; height: 409px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 409px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1140px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1140px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1140px; height: 409px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;app.py</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;st</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;pd</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;np</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;plt</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;seaborn&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;sns</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;sklearn.preprocessing&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;StandardScaler</span><span class="mtk14">,</span><span class="mtk1">&nbsp;LabelEncoder</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;scipy.cluster.hierarchy&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;linkage</span><span class="mtk14">,</span><span class="mtk1">&nbsp;dendrogram</span><span class="mtk14">,</span><span class="mtk1">&nbsp;fcluster</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;sklearn.decomposition&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;PCA</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Title</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Customer&nbsp;Segmentation&nbsp;using&nbsp;Hierarchical&nbsp;Clusteri</span><span class="mtk5">ng"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;pd.read_csv</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Customer_Segmentation_Dataset.csv"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">st.subheader</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Raw&nbsp;Dataset"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df.head</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df.shape</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1126px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1126px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="21" height="613" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 409px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 409px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 409px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1146px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1146px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 409px;"><div class="minimap-shadow-hidden" style="height: 409px;"></div><canvas width="0" height="613" style="position: absolute; left: 0px; width: 0px; height: 409px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="613" style="position: absolute; left: 0px; width: 0px; height: 409px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1272px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 756.36px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-6 output_text"><pre>2025-05-20 14:30:03.357 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:03.358 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:03.372 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:03.373 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:03.381 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:03.382 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
</pre></div><div class="stream output-id-7 output_text"><pre>(2240, 29)
         ID  Year_Birth   Education Marital_Status   Income  Kidhome  \
0      5524        1957  Graduation         Single  58138.0        0   
1      2174        1954  Graduation         Single  46344.0        1   
2      4141        1965  Graduation       Together  71613.0        0   
3      6182        1984  Graduation       Together  26646.0        1   
4      5324        1981         PhD        Married  58293.0        1   
...     ...         ...         ...            ...      ...      ...   
2235  10870        1967  Graduation        Married  61223.0        0   
2236   4001        1946         PhD       Together  64014.0        2   
2237   7270        1981  Graduation       Divorced  56981.0        0   
2238   8235        1956      Master       Together  69245.0        0   
2239   9405        1954         PhD        Married  52869.0        1   

      Teenhome Dt_Customer  Recency  MntWines  ...  NumWebVisitsMonth  \
0            0  04-09-2012       58       635  ...                  7   
1            1  08-03-2014       38        11  ...                  5   
2            0  21-08-2013       26       426  ...                  4   
3            0  10-02-2014       26        11  ...                  6   
4            0  19-01-2014       94       173  ...                  5   
...        ...         ...      ...       ...  ...                ...   
2235         1  13-06-2013       46       709  ...                  5   
2236         1  10-06-2014       56       406  ...                  7   
2237         0  25-01-2014       91       908  ...                  6   
2238         1  24-01-2014        8       428  ...                  3   
2239         1  15-10-2012       40        84  ...                  7   

      AcceptedCmp3  AcceptedCmp4  AcceptedCmp5  AcceptedCmp1  AcceptedCmp2  \
0                0             0             0             0             0   
1                0             0             0             0             0   
2                0             0             0             0             0   
3                0             0             0             0             0   
4                0             0             0             0             0   
...            ...           ...           ...           ...           ...   
2235             0             0             0             0             0   
2236             0             0             0             1             0   
2237             0             1             0             0             0   
2238             0             0             0             0             0   
2239             0             0             0             0             0   

      Complain  Z_CostContact  Z_Revenue  Response  
0            0              3         11         1  
1            0              3         11         0  
2            0              3         11         0  
3            0              3         11         0  
4            0              3         11         0  
...        ...            ...        ...       ...  
2235         0              3         11         0  
2236         0              3         11         0  
2237         0              3         11         0  
2238         0              3         11         0  
2239         0              3         11         1  

[2240 rows x 29 columns]
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$641307570$-->Text
        </md-outlined-button>
        <!--?lit$641307570$-->
      </div><hr>
    </div></div><div class="cell code focused code-has-output" id="cell-3ptW1KTEGXoA" tabindex="-1" role="region" aria-label="Cell 3: Code cell: " style="opacity: 1;"><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$641307570$-->Gemini
    </div><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->arrow_upward</md-icon>
        <!--?lit$641307570$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Move cell up</div><!----><!----><div><!--?lit$641307570$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" aria-disabled="true">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->arrow_downward</md-icon>
        <!--?lit$641307570$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Move cell down</div><!----><!----><div><!--?lit$641307570$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$641307570$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-3ptW1KTEGXoA" anchor="ai-menu-anchor-3ptW1KTEGXoA" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$641307570$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$641307570$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$641307570$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$641307570$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$641307570$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$641307570$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$641307570$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$641307570$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$641307570$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$641307570$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$641307570$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$641307570$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$641307570$-->Explain code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-3ptW1KTEGXoA-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-3ptW1KTEGXoA" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-3ptW1KTEGXoA" id="ai-menu-anchor-3ptW1KTEGXoA-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->link</md-icon>
        <!--?lit$641307570$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Copy link to cell</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->comment</md-icon>
        <!--?lit$641307570$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Add a comment</div><!----><!----><div><!--?lit$641307570$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->settings</md-icon>
        <!--?lit$641307570$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Open editor settings</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->edit</md-icon>
        <!--?lit$641307570$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$641307570$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Mirror cell in tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->delete</md-icon>
        <!--?lit$641307570$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Delete cell</div><!----><!----><div><!--?lit$641307570$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$641307570$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea-and-title">
        <!-- The colab-form-title element is injected here, if it exists. -->
        <div class="inputarea horizontal layout code">
          <div class="cell-gutter">
            <!-- Bounding range for vertical scrolling of icons -->
            <div class="cell-execution-container">
              <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$641307570$--><span class="execution-count"><!--?lit$641307570$-->[13]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$641307570$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$641307570$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$641307570$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell executed since last change

executed by PRIYADHARSHINI _NITT
8:00 PM (0 minutes ago)
executed in 1.528s"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$641307570$-->cell executed since last change</div><!----><!----><br><!----><!----><div><!--?lit$641307570$-->executed by PRIYADHARSHINI _NITT</div><!----><!----><div><!--?lit$641307570$-->8:00 PM (0 minutes ago)</div><!----><!----><div><!--?lit$641307570$-->executed in 1.528s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$641307570$--><div id="status" class="last-run">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>
      <div><!--?lit$641307570$-->1s</div>
    </div>
    </div></template></colab-run-button>
            </div>
          </div>
        <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="24" data-mode-id="notebook-python" style="height: 1568px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/9" style="width: 1146px; height: 1568px;"><div data-mprt="3" class="overflow-guard" style="width: 1146px; height: 1568px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 1568px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 1568px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 1568px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position: absolute; top: 19px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 38px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 57px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 76px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 95px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 114px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 133px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 152px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 171px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 190px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 209px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 228px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 247px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 266px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 285px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 304px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 323px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 342px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 361px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 380px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 399px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 418px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 437px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 456px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 475px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 494px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 513px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 532px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 551px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 570px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 589px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 608px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 627px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 646px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 665px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 684px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 703px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 722px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 741px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 760px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 779px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 798px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 817px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 836px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 855px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 874px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 893px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 912px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 931px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 950px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 969px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 988px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1007px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1026px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1045px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1064px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1083px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1102px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1121px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1140px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1159px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1178px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1197px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1216px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1235px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1254px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1273px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1292px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1311px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1330px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1349px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1368px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1387px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1406px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1425px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1444px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1463px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1482px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1501px; width: 100%; height: 19px;"></div><div style="position:absolute;top:1520px;width:100%;height:19px;"></div><div style="position:absolute;top:1539px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1140px; height: 1568px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1568px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1140px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position: absolute; top: 19px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 38px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 57px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 76px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 95px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 114px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 133px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 152px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 171px; width: 100%; height: 19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position: absolute; top: 209px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 228px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 247px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 266px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 285px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 304px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 323px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 342px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 361px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 380px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 399px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 418px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 437px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 456px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 475px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 494px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 513px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 532px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 551px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 570px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 589px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 608px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 627px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 646px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 665px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 684px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 703px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 722px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 741px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 760px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 779px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 798px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 817px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 836px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 855px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 874px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 893px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 912px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 931px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 950px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 969px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 988px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1007px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1026px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1045px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1064px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1083px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1102px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1121px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1140px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1159px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1178px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1197px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1216px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1235px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1254px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1273px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1292px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1311px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1330px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1349px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1368px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1387px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1406px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1425px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1444px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1463px; width: 100%; height: 19px;"></div><div style="position:absolute;top:1482px;width:100%;height:19px;"></div><div style="position: absolute; top: 1501px; width: 100%; height: 19px;"></div><div style="position: absolute; top: 1520px; width: 100%; height: 19px;"></div><div style="position:absolute;top:1539px;width:100%;height:19px;"><div class="current-line" style="width:1140px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 1568px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1140px; height: 1568px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk1">st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Customer&nbsp;Segmentation&nbsp;with&nbsp;Hierarchical&nbsp;Clusterin</span><span class="mtk5">g&nbsp;and&nbsp;PCA"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 19px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 38px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Assume&nbsp;df&nbsp;is&nbsp;already&nbsp;loaded&nbsp;in&nbsp;your&nbsp;environment</span></span></div><div style="top: 57px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 76px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Drop&nbsp;irrelevant&nbsp;columns</span></span></div><div style="top: 95px; height: 19px;" class="view-line"><span><span class="mtk1">drop_cols&nbsp;=&nbsp;</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">'ID'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Dt_Customer'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'AcceptedCmp1'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'AcceptedCmp2'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'AcceptedCmp3'</span><span class="mtk14">,</span></span></div><div style="top: 114px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'AcceptedCmp4'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'AcceptedCmp5'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Response'</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top: 133px; height: 19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;df.drop</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">columns=drop_cols</span><span class="mtk14">,</span><span class="mtk1">&nbsp;errors=</span><span class="mtk5">'ignore'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 152px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 171px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Create&nbsp;Age&nbsp;from&nbsp;Year_Birth</span></span></div><div style="top: 190px; height: 19px;" class="view-line"><span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">'Age'</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;</span><span class="mtk6">2025</span><span class="mtk1">&nbsp;-&nbsp;df</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">'Year_Birth'</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top: 209px; height: 19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;df.drop</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">columns=</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Year_Birth'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 228px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 247px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Fill&nbsp;missing&nbsp;numeric&nbsp;values&nbsp;with&nbsp;median</span></span></div><div style="top: 266px; height: 19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;df.fillna</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df.median</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">numeric_only=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 285px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 304px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;One-hot&nbsp;encode&nbsp;Education&nbsp;and&nbsp;Marital_Status</span></span></div><div style="top: 323px; height: 19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;pd.get_dummies</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk14">,</span><span class="mtk1">&nbsp;columns=</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Education'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Marital_Status'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14">,</span><span class="mtk1">&nbsp;drop_first=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 342px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 361px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Total&nbsp;spending&nbsp;feature</span></span></div><div style="top: 380px; height: 19px;" class="view-line"><span><span class="mtk1">spending_cols&nbsp;=&nbsp;</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk1">c&nbsp;</span><span class="mtk20">for</span><span class="mtk1">&nbsp;c&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;df.columns&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;c.startswith</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">'Mnt'</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top: 399px; height: 19px;" class="view-line"><span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">'Total_Spending'</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;df</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk1">spending_cols</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">.</span><span class="mtk17">sum</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">axis=</span><span class="mtk6">1</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 418px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 437px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Select&nbsp;features&nbsp;for&nbsp;clustering</span></span></div><div style="top: 456px; height: 19px;" class="view-line"><span><span class="mtk1">features&nbsp;=&nbsp;</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">'Age'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Income'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Kidhome'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Teenhome'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Recency'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Complain'</span><span class="mtk14">,</span></span></div><div style="top: 475px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'NumDealsPurchases'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'NumWebPurchases'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'NumCatalogPurchases'</span><span class="mtk14">,</span></span></div><div style="top: 494px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">'NumStorePurchases'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'NumWebVisitsMonth'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'Total_Spending'</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;+&nbsp;\</span></span></div><div style="top: 513px; height: 19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk1">c&nbsp;</span><span class="mtk20">for</span><span class="mtk1">&nbsp;c&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;df.columns&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;c.startswith</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">'Education_'</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">or</span><span class="mtk1">&nbsp;c.startswith</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">'Marital_Status_'</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top: 532px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 551px; height: 19px;" class="view-line"><span><span class="mtk1">df_features&nbsp;=&nbsp;df</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk1">features</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top: 570px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 589px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Scale&nbsp;features</span></span></div><div style="top: 608px; height: 19px;" class="view-line"><span><span class="mtk1">scaler&nbsp;=&nbsp;StandardScaler</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 627px; height: 19px;" class="view-line"><span><span class="mtk1">scaled_features&nbsp;=&nbsp;scaler.fit_transform</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df_features</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 646px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 665px; height: 19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"###&nbsp;Features&nbsp;after&nbsp;scaling"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 684px; height: 19px;" class="view-line"><span><span class="mtk1">st.dataframe</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">pd.DataFrame</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">scaled_features</span><span class="mtk14">,</span><span class="mtk1">&nbsp;columns=features</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk1">.head</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 703px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 722px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Apply&nbsp;PCA&nbsp;to&nbsp;reduce&nbsp;dimensions&nbsp;to&nbsp;2&nbsp;for&nbsp;visualiz</span><span class="mtk8">ation</span></span></div><div style="top: 741px; height: 19px;" class="view-line"><span><span class="mtk1">pca&nbsp;=&nbsp;PCA</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">n_components=</span><span class="mtk6">2</span><span class="mtk14">,</span><span class="mtk1">&nbsp;random_state=</span><span class="mtk6">42</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 760px; height: 19px;" class="view-line"><span><span class="mtk1">pca_features&nbsp;=&nbsp;pca.fit_transform</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">scaled_features</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 779px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 798px; height: 19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"Explained&nbsp;variance&nbsp;by&nbsp;PCA&nbsp;components:&nbsp;</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">pca.explained_variance_ratio_</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 817px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 836px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Plot&nbsp;PCA&nbsp;scatter&nbsp;before&nbsp;clustering</span></span></div><div style="top: 855px; height: 19px;" class="view-line"><span><span class="mtk1">plt.figure</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">figsize=</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk6">8</span><span class="mtk14">,</span><span class="mtk6">6</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 874px; height: 19px;" class="view-line"><span><span class="mtk1">sns.scatterplot</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">x=pca_features</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk14">:,</span><span class="mtk6">0</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14">,</span><span class="mtk1">&nbsp;y=pca_features</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk14">:,</span><span class="mtk6">1</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 893px; height: 19px;" class="view-line"><span><span class="mtk1">plt.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'PCA&nbsp;Scatter&nbsp;Plot&nbsp;(2&nbsp;Components)'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 912px; height: 19px;" class="view-line"><span><span class="mtk1">st.pyplot</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">plt.gcf</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 931px; height: 19px;" class="view-line"><span><span class="mtk1">plt.clf</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 950px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 969px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Perform&nbsp;hierarchical&nbsp;clustering&nbsp;on&nbsp;scaled&nbsp;data&nbsp;(</span><span class="mtk8">not&nbsp;PCA)</span></span></div><div style="top: 988px; height: 19px;" class="view-line"><span><span class="mtk1">linked&nbsp;=&nbsp;linkage</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">scaled_features</span><span class="mtk14">,</span><span class="mtk1">&nbsp;method=</span><span class="mtk5">'ward'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1007px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 1026px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Plot&nbsp;dendrogram&nbsp;(truncated&nbsp;for&nbsp;clarity)</span></span></div><div style="top: 1045px; height: 19px;" class="view-line"><span><span class="mtk1">plt.figure</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">figsize=</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk6">10</span><span class="mtk14">,</span><span class="mtk6">5</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1064px; height: 19px;" class="view-line"><span><span class="mtk1">dendrogram</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">linked</span><span class="mtk14">,</span><span class="mtk1">&nbsp;truncate_mode=</span><span class="mtk5">'level'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;p=</span><span class="mtk6">5</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1083px; height: 19px;" class="view-line"><span><span class="mtk1">plt.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Hierarchical&nbsp;Clustering&nbsp;Dendrogram&nbsp;(truncated)'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1102px; height: 19px;" class="view-line"><span><span class="mtk1">plt.xlabel</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Sample&nbsp;index&nbsp;or&nbsp;cluster&nbsp;size'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1121px; height: 19px;" class="view-line"><span><span class="mtk1">plt.ylabel</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'Distance'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1140px; height: 19px;" class="view-line"><span><span class="mtk1">st.pyplot</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">plt.gcf</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1159px; height: 19px;" class="view-line"><span><span class="mtk1">plt.clf</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1178px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 1197px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Select&nbsp;number&nbsp;of&nbsp;clusters</span></span></div><div style="top: 1216px; height: 19px;" class="view-line"><span><span class="mtk1">n_clusters&nbsp;=&nbsp;st.slider</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Select&nbsp;number&nbsp;of&nbsp;clusters"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">2</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">10</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">4</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1235px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 1254px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Get&nbsp;cluster&nbsp;labels</span></span></div><div style="top: 1273px; height: 19px;" class="view-line"><span><span class="mtk1">cluster_labels&nbsp;=&nbsp;fcluster</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">linked</span><span class="mtk14">,</span><span class="mtk1">&nbsp;t=n_clusters</span><span class="mtk14">,</span><span class="mtk1">&nbsp;criterion=</span><span class="mtk5">'maxclust'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1292px; height: 19px;" class="view-line"><span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">'Cluster'</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;cluster_labels</span></span></div><div style="top: 1311px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 1330px; height: 19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"###&nbsp;Cluster&nbsp;counts"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1349px; height: 19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Cluster'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk1">.value_counts</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk1">.sort_index</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1368px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 1387px; height: 19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"###&nbsp;Cluster&nbsp;summary&nbsp;(mean&nbsp;values)"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1406px; height: 19px;" class="view-line"><span><span class="mtk1">st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df.groupby</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">'Cluster'</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk1">features</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk1">.mean</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk1">.</span><span class="mtk17">round</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk6">2</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1425px; height: 19px;" class="view-line"><span><span></span></span></div><div style="top: 1444px; height: 19px;" class="view-line"><span><span class="mtk8">#&nbsp;Plot&nbsp;PCA&nbsp;scatter&nbsp;colored&nbsp;by&nbsp;cluster</span></span></div><div style="top: 1463px; height: 19px;" class="view-line"><span><span class="mtk1">plt.figure</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">figsize=</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk6">8</span><span class="mtk14">,</span><span class="mtk6">6</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1482px; height: 19px;" class="view-line"><span><span class="mtk1">sns.scatterplot</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">x=pca_features</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk14">:,</span><span class="mtk6">0</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14">,</span><span class="mtk1">&nbsp;y=pca_features</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk14">:,</span><span class="mtk6">1</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14">,</span><span class="mtk1">&nbsp;hue=cluster_labels</span><span class="mtk14">,</span><span class="mtk1">&nbsp;palette=</span><span class="mtk5">'Set2'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;s=</span><span class="mtk6">50</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1501px; height: 19px;" class="view-line"><span><span class="mtk1">plt.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'PCA&nbsp;Scatter&nbsp;Plot&nbsp;colored&nbsp;by&nbsp;Cluster'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1520px; height: 19px;" class="view-line"><span><span class="mtk1">st.pyplot</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">plt.gcf</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top: 1539px; height: 19px;" class="view-line"><span><span class="mtk1">plt.clf</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk14 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"><div class="lightBulbWidget codicon codicon-light-bulb" widgetid="LightBulbWidget" title="Show Code Actions (Ctrl+.)" style="position: absolute; display: none; visibility: hidden; max-width: 1140px;"></div></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 1539px; left: 68px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 1px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1126px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1126px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="21" height="2352" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 1568px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 1568px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 1568px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1146px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 1539px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1146px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 1568px;"><div class="minimap-shadow-hidden" style="height: 1568px;"></div><canvas width="0" height="2352" style="position: absolute; left: 0px; width: 0px; height: 1568px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="2352" style="position: absolute; left: 0px; width: 0px; height: 1568px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 403px; width: 758px; z-index: 50; display: none; visibility: hidden; max-width: 1272px; top: 309.417px; left: 107.667px;"><div class="monaco-sash vertical" style="left: 756px;"></div><div class="monaco-sash vertical disabled" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal disabled" style="top: -2px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 401px;"><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip" style="width: 758px; height: 403px;"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 756.36px; max-height: 392px; width: 758px; height: 403px; padding-bottom: 10px;"><div class="hover-row markdown-hover"><div class="hover-contents code-hover-contents"><div class="rendered-markdown"><div data-code="id#36"><span style="font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px;"><div class="monaco-tokenized-source"><span class="mtk19">def</span><span class="mtk1"> scatterplot</span><span class="mtk14">(</span><span class="mtk1">data=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> *</span><span class="mtk14">,</span><span class="mtk1"> x=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> y=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> hue=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> size=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> style=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> palette=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> hue_order=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> hue_norm=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> sizes=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> size_order=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> size_norm=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> markers=</span><span class="mtk19">True</span><span class="mtk14">,</span><span class="mtk1"> style_order=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> legend=</span><span class="mtk5">'auto'</span><span class="mtk14">,</span><span class="mtk1"> ax=</span><span class="mtk19">None</span><span class="mtk14">,</span><span class="mtk1"> **kwargs</span><span class="mtk14">)</span></div></span></div></div></div></div><div class="hover-row markdown-hover"><div class="hover-contents"><div class="rendered-markdown"><p><a data-href="command:pinDocumentation?%5B%22sns.scatterplot%22%2C%22%60%60%60python%5Cndef%20scatterplot(data%3DNone%2C%20*%2C%20x%3DNone%2C%20y%3DNone%2C%20hue%3DNone%2C%20size%3DNone%2C%20style%3DNone%2C%20palette%3DNone%2C%20hue_order%3DNone%2C%20hue_norm%3DNone%2C%20sizes%3DNone%2C%20size_order%3DNone%2C%20size_norm%3DNone%2C%20markers%3DTrue%2C%20style_order%3DNone%2C%20legend%3D&#39;auto&#39;%2C%20ax%3DNone%2C%20**kwargs)%5Cn%60%60%60%5Cn%5CnDraw%20a%20scatter%20plot%20with%20possibility%20of%20several%20semantic%20groupings.%5Cn%5CnThe%20relationship%20between%20%60x%60%20and%20%60y%60%20can%20be%20shown%20for%20different%20subsets%5Cnof%20the%20data%20using%20the%20%60hue%60%2C%20%60size%60%2C%20and%20%60style%60%20parameters.%20These%5Cnparameters%20control%20what%20visual%20semantics%20are%20used%20to%20identify%20the%20different%5Cnsubsets.%20It%20is%20possible%20to%20show%20up%20to%20three%20dimensions%20independently%20by%5Cnusing%20all%20three%20semantic%20types%2C%20but%20this%20style%20of%20plot%20can%20be%20hard%20to%5Cninterpret%20and%20is%20often%20ineffective.%20Using%20redundant%20semantics%20(i.e.%20both%5Cn%60hue%60%20and%20%60style%60%20for%20the%20same%20variable)%20can%20be%20helpful%20for%20making%5Cngraphics%20more%20accessible.%5Cn%5CnSee%20the%20%60tutorial%20%3Crelational_tutorial%3E%60%20for%20more%20information.%5Cn%5CnThe%20default%20treatment%20of%20the%20%60hue%60%20(and%20to%20a%20lesser%20extent%2C%20%60size%60)%5Cnsemantic%2C%20if%20present%2C%20depends%20on%20whether%20the%20variable%20is%20inferred%20to%5Cnrepresent%20%5C%22numeric%5C%22%20or%20%5C%22categorical%5C%22%20data.%20In%20particular%2C%20numeric%20variables%5Cnare%20represented%20with%20a%20sequential%20colormap%20by%20default%2C%20and%20the%20legend%5Cnentries%20show%20regular%20%5C%22ticks%5C%22%20with%20values%20that%20may%20or%20may%20not%20exist%20in%20the%5Cndata.%20This%20behavior%20can%20be%20controlled%20through%20various%20parameters%2C%20as%5Cndescribed%20and%20illustrated%20below.%5Cn%5CnParameters%5Cn----------%5Cndata%20%3A%20%60pandas.DataFrame%60%2C%20%60numpy.ndarray%60%2C%20mapping%2C%20or%20sequence%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BInput%20data%20structure.%20Either%20a%20long-form%20collection%20of%20vectors%20that%20can%20be%5Cnassigned%20to%20named%20variables%20or%20a%20wide-form%20dataset%20that%20will%20be%20internally%5Cnreshaped.%20%20%5Cnx%2C%20y%20%3A%20vectors%20or%20keys%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BVariables%20that%20specify%20positions%20on%20the%20x%20and%20y%20axes.%20%20%5Cnhue%20%3A%20vector%20or%20key%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BGrouping%20variable%20that%20will%20produce%20points%20with%20different%20colors.%5CnCan%20be%20either%20categorical%20or%20numeric%2C%20although%20color%20mapping%20will%5Cnbehave%20differently%20in%20latter%20case.%20%20%5Cnsize%20%3A%20vector%20or%20key%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BGrouping%20variable%20that%20will%20produce%20points%20with%20different%20sizes.%5CnCan%20be%20either%20categorical%20or%20numeric%2C%20although%20size%20mapping%20will%5Cnbehave%20differently%20in%20latter%20case.%20%20%5Cnstyle%20%3A%20vector%20or%20key%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BGrouping%20variable%20that%20will%20produce%20points%20with%20different%20markers.%5CnCan%20have%20a%20numeric%20dtype%20but%20will%20always%20be%20treated%20as%20categorical.%20%20%5Cnpalette%20%3A%20string%2C%20list%2C%20dict%2C%20or%20%60matplotlib.colors.Colormap%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BMethod%20for%20choosing%20the%20colors%20to%20use%20when%20mapping%20the%20%60hue%60%20semantic.%5CnString%20values%20are%20passed%20to%20%60color_palette%60.%20List%20or%20dict%20values%5Cnimply%20categorical%20mapping%2C%20while%20a%20colormap%20object%20implies%20numeric%20mapping.%20%20%5Cnhue%5C%5C_order%20%3A%20vector%20of%20strings%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BSpecify%20the%20order%20of%20processing%20and%20plotting%20for%20categorical%20levels%20of%20the%5Cn%60hue%60%20semantic.%20%20%5Cnhue%5C%5C_norm%20%3A%20tuple%20or%20%60matplotlib.colors.Normalize%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BEither%20a%20pair%20of%20values%20that%20set%20the%20normalization%20range%20in%20data%20units%5Cnor%20an%20object%20that%20will%20map%20from%20data%20units%20into%20a%20%5C%5C%5B0%2C%201%5C%5C%5D%20interval.%20Usage%5Cnimplies%20numeric%20mapping.%20%20%5Cnsizes%20%3A%20list%2C%20dict%2C%20or%20tuple%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BAn%20object%20that%20determines%20how%20sizes%20are%20chosen%20when%20%60size%60%20is%20used.%5CnList%20or%20dict%20arguments%20should%20provide%20a%20size%20for%20each%20unique%20data%20value%2C%5Cnwhich%20forces%20a%20categorical%20interpretation.%20The%20argument%20may%20also%20be%20a%5Cnmin%2C%20max%20tuple.%20%20%5Cnsize%5C%5C_order%20%3A%20list%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BSpecified%20order%20for%20appearance%20of%20the%20%60size%60%20variable%20levels%2C%5Cnotherwise%20they%20are%20determined%20from%20the%20data.%20Not%20relevant%20when%20the%5Cn%60size%60%20variable%20is%20numeric.%20%20%5Cnsize%5C%5C_norm%20%3A%20tuple%20or%20Normalize%20object%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BNormalization%20in%20data%20units%20for%20scaling%20plot%20objects%20when%20the%5Cn%60size%60%20variable%20is%20numeric.%20%20%5Cnmarkers%20%3A%20boolean%2C%20list%2C%20or%20dictionary%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BObject%20determining%20how%20to%20draw%20the%20markers%20for%20different%20levels%20of%20the%5Cn%60style%60%20variable.%20Setting%20to%20%60True%60%20will%20use%20default%20markers%2C%20or%5Cnyou%20can%20pass%20a%20list%20of%20markers%20or%20a%20dictionary%20mapping%20levels%20of%20the%5Cn%60style%60%20variable%20to%20markers.%20Setting%20to%20%60False%60%20will%20draw%5Cnmarker-less%20lines.%20%20Markers%20are%20specified%20as%20in%20matplotlib.%20%20%5Cnstyle%5C%5C_order%20%3A%20list%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BSpecified%20order%20for%20appearance%20of%20the%20%60style%60%20variable%20levels%5Cnotherwise%20they%20are%20determined%20from%20the%20data.%20Not%20relevant%20when%20the%5Cn%60style%60%20variable%20is%20numeric.%20%20%5Cnlegend%20%3A%20%5C%22auto%5C%22%2C%20%5C%22brief%5C%22%2C%20%5C%22full%5C%22%2C%20or%20False%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BHow%20to%20draw%20the%20legend.%20If%20%5C%22brief%5C%22%2C%20numeric%20%60hue%60%20and%20%60size%60%5Cnvariables%20will%20be%20represented%20with%20a%20sample%20of%20evenly%20spaced%20values.%5CnIf%20%5C%22full%5C%22%2C%20every%20group%20will%20get%20an%20entry%20in%20the%20legend.%20If%20%5C%22auto%5C%22%2C%5Cnchoose%20between%20brief%20or%20full%20representation%20based%20on%20number%20of%20levels.%5CnIf%20%60False%60%2C%20no%20legend%20data%20is%20added%20and%20no%20legend%20is%20drawn.%20%20%5Cnax%20%3A%20%60matplotlib.axes.Axes%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BPre-existing%20axes%20for%20the%20plot.%20Otherwise%2C%20call%20%60matplotlib.pyplot.gca%60%5Cninternally.%20%20%5Cnkwargs%20%3A%20key%2C%20value%20mappings%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BOther%20keyword%20arguments%20are%20passed%20down%20to%5Cn%60matplotlib.axes.Axes.scatter%60.%5Cn%5CnReturns%5Cn-------%5Cn%60matplotlib.axes.Axes%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BThe%20matplotlib%20axes%20containing%20the%20plot.%5Cn%5CnSee%20Also%5Cn--------%5Cnlineplot%20%3A%20Plot%20data%20using%20lines.%20%20%5Cnstripplot%20%3A%20Plot%20a%20categorical%20scatter%20with%20jitter.%20%20%5Cnswarmplot%20%3A%20Plot%20a%20categorical%20scatter%20with%20non-overlapping%20points.%5Cn%5CnExamples%5Cn--------%22%5D" href="https://colab.research.google.com/drive/1PCga96CMC_NQg61iq2IiLVF7R0IXtb7w" title="command:pinDocumentation?%5B%22sns.scatterplot%22%2C%22%60%60%60python%5Cndef%20scatterplot(data%3DNone%2C%20*%2C%20x%3DNone%2C%20y%3DNone%2C%20hue%3DNone%2C%20size%3DNone%2C%20style%3DNone%2C%20palette%3DNone%2C%20hue_order%3DNone%2C%20hue_norm%3DNone%2C%20sizes%3DNone%2C%20size_order%3DNone%2C%20size_norm%3DNone%2C%20markers%3DTrue%2C%20style_order%3DNone%2C%20legend%3D&#39;auto&#39;%2C%20ax%3DNone%2C%20**kwargs)%5Cn%60%60%60%5Cn%5CnDraw%20a%20scatter%20plot%20with%20possibility%20of%20several%20semantic%20groupings.%5Cn%5CnThe%20relationship%20between%20%60x%60%20and%20%60y%60%20can%20be%20shown%20for%20different%20subsets%5Cnof%20the%20data%20using%20the%20%60hue%60%2C%20%60size%60%2C%20and%20%60style%60%20parameters.%20These%5Cnparameters%20control%20what%20visual%20semantics%20are%20used%20to%20identify%20the%20different%5Cnsubsets.%20It%20is%20possible%20to%20show%20up%20to%20three%20dimensions%20independently%20by%5Cnusing%20all%20three%20semantic%20types%2C%20but%20this%20style%20of%20plot%20can%20be%20hard%20to%5Cninterpret%20and%20is%20often%20ineffective.%20Using%20redundant%20semantics%20(i.e.%20both%5Cn%60hue%60%20and%20%60style%60%20for%20the%20same%20variable)%20can%20be%20helpful%20for%20making%5Cngraphics%20more%20accessible.%5Cn%5CnSee%20the%20%60tutorial%20%3Crelational_tutorial%3E%60%20for%20more%20information.%5Cn%5CnThe%20default%20treatment%20of%20the%20%60hue%60%20(and%20to%20a%20lesser%20extent%2C%20%60size%60)%5Cnsemantic%2C%20if%20present%2C%20depends%20on%20whether%20the%20variable%20is%20inferred%20to%5Cnrepresent%20%5C%22numeric%5C%22%20or%20%5C%22categorical%5C%22%20data.%20In%20particular%2C%20numeric%20variables%5Cnare%20represented%20with%20a%20sequential%20colormap%20by%20default%2C%20and%20the%20legend%5Cnentries%20show%20regular%20%5C%22ticks%5C%22%20with%20values%20that%20may%20or%20may%20not%20exist%20in%20the%5Cndata.%20This%20behavior%20can%20be%20controlled%20through%20various%20parameters%2C%20as%5Cndescribed%20and%20illustrated%20below.%5Cn%5CnParameters%5Cn----------%5Cndata%20%3A%20%60pandas.DataFrame%60%2C%20%60numpy.ndarray%60%2C%20mapping%2C%20or%20sequence%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BInput%20data%20structure.%20Either%20a%20long-form%20collection%20of%20vectors%20that%20can%20be%5Cnassigned%20to%20named%20variables%20or%20a%20wide-form%20dataset%20that%20will%20be%20internally%5Cnreshaped.%20%20%5Cnx%2C%20y%20%3A%20vectors%20or%20keys%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BVariables%20that%20specify%20positions%20on%20the%20x%20and%20y%20axes.%20%20%5Cnhue%20%3A%20vector%20or%20key%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BGrouping%20variable%20that%20will%20produce%20points%20with%20different%20colors.%5CnCan%20be%20either%20categorical%20or%20numeric%2C%20although%20color%20mapping%20will%5Cnbehave%20differently%20in%20latter%20case.%20%20%5Cnsize%20%3A%20vector%20or%20key%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BGrouping%20variable%20that%20will%20produce%20points%20with%20different%20sizes.%5CnCan%20be%20either%20categorical%20or%20numeric%2C%20although%20size%20mapping%20will%5Cnbehave%20differently%20in%20latter%20case.%20%20%5Cnstyle%20%3A%20vector%20or%20key%20in%20%60data%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BGrouping%20variable%20that%20will%20produce%20points%20with%20different%20markers.%5CnCan%20have%20a%20numeric%20dtype%20but%20will%20always%20be%20treated%20as%20categorical.%20%20%5Cnpalette%20%3A%20string%2C%20list%2C%20dict%2C%20or%20%60matplotlib.colors.Colormap%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BMethod%20for%20choosing%20the%20colors%20to%20use%20when%20mapping%20the%20%60hue%60%20semantic.%5CnString%20values%20are%20passed%20to%20%60color_palette%60.%20List%20or%20dict%20values%5Cnimply%20categorical%20mapping%2C%20while%20a%20colormap%20object%20implies%20numeric%20mapping.%20%20%5Cnhue%5C%5C_order%20%3A%20vector%20of%20strings%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BSpecify%20the%20order%20of%20processing%20and%20plotting%20for%20categorical%20levels%20of%20the%5Cn%60hue%60%20semantic.%20%20%5Cnhue%5C%5C_norm%20%3A%20tuple%20or%20%60matplotlib.colors.Normalize%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BEither%20a%20pair%20of%20values%20that%20set%20the%20normalization%20range%20in%20data%20units%5Cnor%20an%20object%20that%20will%20map%20from%20data%20units%20into%20a%20%5C%5C%5B0%2C%201%5C%5C%5D%20interval.%20Usage%5Cnimplies%20numeric%20mapping.%20%20%5Cnsizes%20%3A%20list%2C%20dict%2C%20or%20tuple%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BAn%20object%20that%20determines%20how%20sizes%20are%20chosen%20when%20%60size%60%20is%20used.%5CnList%20or%20dict%20arguments%20should%20provide%20a%20size%20for%20each%20unique%20data%20value%2C%5Cnwhich%20forces%20a%20categorical%20interpretation.%20The%20argument%20may%20also%20be%20a%5Cnmin%2C%20max%20tuple.%20%20%5Cnsize%5C%5C_order%20%3A%20list%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BSpecified%20order%20for%20appearance%20of%20the%20%60size%60%20variable%20levels%2C%5Cnotherwise%20they%20are%20determined%20from%20the%20data.%20Not%20relevant%20when%20the%5Cn%60size%60%20variable%20is%20numeric.%20%20%5Cnsize%5C%5C_norm%20%3A%20tuple%20or%20Normalize%20object%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BNormalization%20in%20data%20units%20for%20scaling%20plot%20objects%20when%20the%5Cn%60size%60%20variable%20is%20numeric.%20%20%5Cnmarkers%20%3A%20boolean%2C%20list%2C%20or%20dictionary%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BObject%20determining%20how%20to%20draw%20the%20markers%20for%20different%20levels%20of%20the%5Cn%60style%60%20variable.%20Setting%20to%20%60True%60%20will%20use%20default%20markers%2C%20or%5Cnyou%20can%20pass%20a%20list%20of%20markers%20or%20a%20dictionary%20mapping%20levels%20of%20the%5Cn%60style%60%20variable%20to%20markers.%20Setting%20to%20%60False%60%20will%20draw%5Cnmarker-less%20lines.%20%20Markers%20are%20specified%20as%20in%20matplotlib.%20%20%5Cnstyle%5C%5C_order%20%3A%20list%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BSpecified%20order%20for%20appearance%20of%20the%20%60style%60%20variable%20levels%5Cnotherwise%20they%20are%20determined%20from%20the%20data.%20Not%20relevant%20when%20the%5Cn%60style%60%20variable%20is%20numeric.%20%20%5Cnlegend%20%3A%20%5C%22auto%5C%22%2C%20%5C%22brief%5C%22%2C%20%5C%22full%5C%22%2C%20or%20False%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BHow%20to%20draw%20the%20legend.%20If%20%5C%22brief%5C%22%2C%20numeric%20%60hue%60%20and%20%60size%60%5Cnvariables%20will%20be%20represented%20with%20a%20sample%20of%20evenly%20spaced%20values.%5CnIf%20%5C%22full%5C%22%2C%20every%20group%20will%20get%20an%20entry%20in%20the%20legend.%20If%20%5C%22auto%5C%22%2C%5Cnchoose%20between%20brief%20or%20full%20representation%20based%20on%20number%20of%20levels.%5CnIf%20%60False%60%2C%20no%20legend%20data%20is%20added%20and%20no%20legend%20is%20drawn.%20%20%5Cnax%20%3A%20%60matplotlib.axes.Axes%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BPre-existing%20axes%20for%20the%20plot.%20Otherwise%2C%20call%20%60matplotlib.pyplot.gca%60%5Cninternally.%20%20%5Cnkwargs%20%3A%20key%2C%20value%20mappings%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BOther%20keyword%20arguments%20are%20passed%20down%20to%5Cn%60matplotlib.axes.Axes.scatter%60.%5Cn%5CnReturns%5Cn-------%5Cn%60matplotlib.axes.Axes%60%20%20%5Cn%26nbsp%3B%26nbsp%3B%26nbsp%3B%26nbsp%3BThe%20matplotlib%20axes%20containing%20the%20plot.%5Cn%5CnSee%20Also%5Cn--------%5Cnlineplot%20%3A%20Plot%20data%20using%20lines.%20%20%5Cnstripplot%20%3A%20Plot%20a%20categorical%20scatter%20with%20jitter.%20%20%5Cnswarmplot%20%3A%20Plot%20a%20categorical%20scatter%20with%20non-overlapping%20points.%5Cn%5CnExamples%5Cn--------%22%5D">Open in tab</a>     <a data-href="command:viewSource?%5B%22file%3A%2F%2F%2Fusr%2Flocal%2Flib%2Fpython3.11%2Fdist-packages%2Fseaborn%2Frelational.py%22%2C%7B%22startLineNumber%22%3A606%2C%22startColumn%22%3A1%2C%22endLineNumber%22%3A606%2C%22endColumn%22%3A1%7D%5D" href="https://colab.research.google.com/drive/1PCga96CMC_NQg61iq2IiLVF7R0IXtb7w" title="command:viewSource?%5B%22file%3A%2F%2F%2Fusr%2Flocal%2Flib%2Fpython3.11%2Fdist-packages%2Fseaborn%2Frelational.py%22%2C%7B%22startLineNumber%22%3A606%2C%22startColumn%22%3A1%2C%22endLineNumber%22%3A606%2C%22endColumn%22%3A1%7D%5D">View source</a></p></div></div></div><div class="hover-row markdown-hover"><div class="hover-contents"><div class="rendered-markdown"><p>Draw a scatter plot with possibility of several semantic groupings.</p><p>The relationship between <code>x</code> and <code>y</code> can be shown for different subsets
of the data using the <code>hue</code>, <code>size</code>, and <code>style</code> parameters. These
parameters control what visual semantics are used to identify the different
subsets. It is possible to show up to three dimensions independently by
using all three semantic types, but this style of plot can be hard to
interpret and is often ineffective. Using redundant semantics (i.e. both
<code>hue</code> and <code>style</code> for the same variable) can be helpful for making
graphics more accessible.</p><p>See the <code>tutorial &lt;relational_tutorial&gt;</code> for more information.</p><p>The default treatment of the <code>hue</code> (and to a lesser extent, <code>size</code>)
semantic, if present, depends on whether the variable is inferred to
represent "numeric" or "categorical" data. In particular, numeric variables
are represented with a sequential colormap by default, and the legend
entries show regular "ticks" with values that may or may not exist in the
data. This behavior can be controlled through various parameters, as
described and illustrated below.</p><h2>Parameters</h2>
<p>data : <code>pandas.DataFrame</code>, <code>numpy.ndarray</code>, mapping, or sequence<br>&nbsp;&nbsp;&nbsp;&nbsp;Input data structure. Either a long-form collection of vectors that can be
assigned to named variables or a wide-form dataset that will be internally
reshaped.<br>x, y : vectors or keys in <code>data</code><br>&nbsp;&nbsp;&nbsp;&nbsp;Variables that specify positions on the x and y axes.<br>hue : vector or key in <code>data</code><br>&nbsp;&nbsp;&nbsp;&nbsp;Grouping variable that will produce points with different colors.
Can be either categorical or numeric, although color mapping will
behave differently in latter case.<br>size : vector or key in <code>data</code><br>&nbsp;&nbsp;&nbsp;&nbsp;Grouping variable that will produce points with different sizes.
Can be either categorical or numeric, although size mapping will
behave differently in latter case.<br>style : vector or key in <code>data</code><br>&nbsp;&nbsp;&nbsp;&nbsp;Grouping variable that will produce points with different markers.
Can have a numeric dtype but will always be treated as categorical.<br>palette : string, list, dict, or <code>matplotlib.colors.Colormap</code><br>&nbsp;&nbsp;&nbsp;&nbsp;Method for choosing the colors to use when mapping the <code>hue</code> semantic.
String values are passed to <code>color_palette</code>. List or dict values
imply categorical mapping, while a colormap object implies numeric mapping.<br>hue_order : vector of strings<br>&nbsp;&nbsp;&nbsp;&nbsp;Specify the order of processing and plotting for categorical levels of the
<code>hue</code> semantic.<br>hue_norm : tuple or <code>matplotlib.colors.Normalize</code><br>&nbsp;&nbsp;&nbsp;&nbsp;Either a pair of values that set the normalization range in data units
or an object that will map from data units into a [0, 1] interval. Usage
implies numeric mapping.<br>sizes : list, dict, or tuple<br>&nbsp;&nbsp;&nbsp;&nbsp;An object that determines how sizes are chosen when <code>size</code> is used.
List or dict arguments should provide a size for each unique data value,
which forces a categorical interpretation. The argument may also be a
min, max tuple.<br>size_order : list<br>&nbsp;&nbsp;&nbsp;&nbsp;Specified order for appearance of the <code>size</code> variable levels,
otherwise they are determined from the data. Not relevant when the
<code>size</code> variable is numeric.<br>size_norm : tuple or Normalize object<br>&nbsp;&nbsp;&nbsp;&nbsp;Normalization in data units for scaling plot objects when the
<code>size</code> variable is numeric.<br>markers : boolean, list, or dictionary<br>&nbsp;&nbsp;&nbsp;&nbsp;Object determining how to draw the markers for different levels of the
<code>style</code> variable. Setting to <code>True</code> will use default markers, or
you can pass a list of markers or a dictionary mapping levels of the
<code>style</code> variable to markers. Setting to <code>False</code> will draw
marker-less lines.  Markers are specified as in matplotlib.<br>style_order : list<br>&nbsp;&nbsp;&nbsp;&nbsp;Specified order for appearance of the <code>style</code> variable levels
otherwise they are determined from the data. Not relevant when the
<code>style</code> variable is numeric.<br>legend : "auto", "brief", "full", or False<br>&nbsp;&nbsp;&nbsp;&nbsp;How to draw the legend. If "brief", numeric <code>hue</code> and <code>size</code>
variables will be represented with a sample of evenly spaced values.
If "full", every group will get an entry in the legend. If "auto",
choose between brief or full representation based on number of levels.
If <code>False</code>, no legend data is added and no legend is drawn.<br>ax : <code>matplotlib.axes.Axes</code><br>&nbsp;&nbsp;&nbsp;&nbsp;Pre-existing axes for the plot. Otherwise, call <code>matplotlib.pyplot.gca</code>
internally.<br>kwargs : key, value mappings<br>&nbsp;&nbsp;&nbsp;&nbsp;Other keyword arguments are passed down to
<code>matplotlib.axes.Axes.scatter</code>.</p><h2>Returns</h2>
<p><code>matplotlib.axes.Axes</code><br>&nbsp;&nbsp;&nbsp;&nbsp;The matplotlib axes containing the plot.</p><h2>See Also</h2>
<p>lineplot : Plot data using lines.<br>stripplot : Plot a categorical scatter with jitter.<br>swarmplot : Plot a categorical scatter with non-overlapping points.</p><h2>Examples</h2>
</div></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 746px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 746px;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical fade" style="position: absolute; width: 10px; height: 402px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 81px;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
      </div>
    <div class="output" aria-label="Cell 3 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$--><svg viewBox="0 0 24 24"><!--?lit$641307570$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer" style="min-height: 0px;"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output-id-30 output_text"><pre>2025-05-20 14:30:12.963 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:12.964 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:12.987 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:12.989 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:12.995 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:12.995 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:13.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:13.002 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:13.062 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:13.294 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:13.295 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:13.598 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.023 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.024 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.038 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.039 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.041 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.044 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.045 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.054 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.055 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.060 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.061 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.063 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.064 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.071 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.071 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.120 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.477 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-05-20 14:30:14.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$641307570$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$641307570$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$641307570$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer class="sn-resize no-tabs" style="height: 40%"><div class="resizer-thumb"></div>
        <!--?lit$641307570$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$641307570$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$641307570$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$641307570$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$641307570$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer class="sn-resize no-tabs" style="height: 40%"><div class="resizer-thumb"></div>
        <!--?lit$641307570$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$641307570$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$641307570$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$641307570$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$641307570$--><span class="icon"><slot></slot></span>
        <!--?lit$641307570$-->
        <!--?lit$641307570$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./APP.py - Colab_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./APP.py - Colab_files/outputframe(2).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" class="status-bar-ui-refresh"><template shadowrootmode="open"><!----><span class="left">
          <slot name="bottom-pane-buttons"></slot>
        </span>
        <span class="middle"><!--?lit$641307570$--></span>
        <span class="right">
          <!--?lit$641307570$--><colab-execution-status><template shadowrootmode="open"><!----><md-text-button id="execution-status" aria-describedby="execution-status-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template><!--?lit$641307570$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon><!--?lit$641307570$-->8:00 PM</md-text-button>
      <colab-tooltip-trigger aria-hidden="true" id="execution-status-tooltip" for="execution-status" message="Focus the last run cell

8:00 PM (0 minutes ago)
executed in 1.526s"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Focus the last run cell</div><!----><!----><br><!----><!----><div><!--?lit$641307570$-->8:00 PM (0 minutes ago)</div><!----><!----><div><!--?lit$641307570$-->executed in 1.526s</div><!----><!--?--></template>
      </colab-tooltip-trigger></template></colab-execution-status><!--?lit$641307570$--><!--?lit$641307570$--><!--?lit$641307570$--><colab-runtime-status><template shadowrootmode="open"><!----><md-text-button data-aria-expanded="false" data-aria-haspopup="menu" id="runtime-options" aria-describedby="runtime-options-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button" aria-haspopup="menu" aria-expanded="false">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dns</md-icon><!--?lit$641307570$-->Python 3</md-text-button><colab-tooltip-trigger aria-hidden="true" for="runtime-options" id="runtime-options-tooltip" message="Runtime options"><template shadowrootmode="open"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Runtime options</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-runtime-status>
        </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->data_object</md-icon>
        <!--?lit$641307570$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$641307570$-->terminal</md-icon>
        <!--?lit$641307570$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="locate-in-drive" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Locate in Drive<!--?lit$641307570$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Open in playground mode<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->New notebook in Drive<!--?lit$641307570$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Open notebook<!--?lit$641307570$--></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Upload notebook<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Rename<!--?lit$641307570$--></div></div><div command="move-notebook" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Move<!--?lit$641307570$--></div></div><div command="trash" class=" goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Move to trash<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Save a copy in Drive<!--?lit$641307570$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Save a copy as a GitHub Gist<!--?lit$641307570$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Save a copy in GitHub<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Save<!--?lit$641307570$--></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Save and pin revision<!--?lit$641307570$--></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Revision history<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$641307570$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Print<!--?lit$641307570$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Download .ipynb<!--?lit$641307570$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Download .py<!--?lit$641307570$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Undo<!--?lit$641307570$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Redo<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Select all cells<!--?lit$641307570$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Cut cell or selection<!--?lit$641307570$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Copy cell or selection<!--?lit$641307570$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Paste<!--?lit$641307570$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Delete selected cells<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Find and replace<!--?lit$641307570$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Find next<!--?lit$641307570$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Find previous<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Notebook settings<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Clear all outputs<!--?lit$641307570$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$641307570$-->Table of contents<!--?lit$641307570$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Notebook info<!--?lit$641307570$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Executed code history<!--?lit$641307570$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$641307570$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1e" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Collapse sections<!--?lit$641307570$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Expand sections<!--?lit$641307570$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Save collapsed section layout<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Show/hide code<!--?lit$641307570$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Show/hide output<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1l" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Focus next tab<!--?lit$641307570$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Focus previous tab<!--?lit$641307570$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Move tab to next pane<!--?lit$641307570$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Move tab to previous pane<!--?lit$641307570$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Hide comments<!--?lit$641307570$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Minimize comments<!--?lit$641307570$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Expand comments<!--?lit$641307570$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Code cell<!--?lit$641307570$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Text cell<!--?lit$641307570$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Section header cell<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Scratch code cell<!--?lit$641307570$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Code snippets<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1x" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Add a form field<!--?lit$641307570$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Run all<!--?lit$641307570$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Run before<!--?lit$641307570$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Run the focused cell<!--?lit$641307570$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Run selection<!--?lit$641307570$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Run cell and below<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":25" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Interrupt execution<!--?lit$641307570$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":27" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Restart session<!--?lit$641307570$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Restart session and run all<!--?lit$641307570$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Disconnect and delete runtime<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2a" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Change runtime type<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Manage sessions<!--?lit$641307570$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->View resources<!--?lit$641307570$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->View runtime logs<!--?lit$641307570$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Command palette<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Settings<!--?lit$641307570$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Keyboard shortcuts<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2l" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Diff notebooks<!--?lit$641307570$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$641307570$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$641307570$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Frequently asked questions<!--?lit$641307570$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->View release notes<!--?lit$641307570$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Search code snippets<!--?lit$641307570$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2r" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Report a bug<!--?lit$641307570$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Report Drive abuse<!--?lit$641307570$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->Send feedback<!--?lit$641307570$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$641307570$-->View terms of service<!--?lit$641307570$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$641307570$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$641307570$--><button id="button" class="button">
      <!--?lit$641307570$-->
      <span class="touch"></span>
      <!--?lit$641307570$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$641307570$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$641307570$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;"></div><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;">*values: object, Prints the values to a stream, or to sys.stdout by default.

sep  
&amp;nbsp;&amp;nbsp;string inserted between values, default a space.  
end  
&amp;nbsp;&amp;nbsp;string appended after the last value, default a newline.  
file  
&amp;nbsp;&amp;nbsp;a file-like object (stream); defaults to the current sys.stdout.  
flush  
&amp;nbsp;&amp;nbsp;whether to forcibly flush the stream., hint</div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy0df0947417c1d587de1f8dcaa51496a3e74b39b20.1411994098" name="apiproxy0df0947417c1d587de1f8dcaa51496a3e74b39b20.1411994098" src="./APP.py - Colab_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-xxdsoekymqfe" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./APP.py - Colab_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./APP.py - Colab_files/saved_resource.html"></iframe></div><iframe src="./APP.py - Colab_files/bscframe.html" style="display: none;"></iframe><colab-callout dismisstext="" tooltipstyling="" aria-label="Rename notebook" opened="" role="tooltip" verticaldirection="below" horizontaldirection="right" style="visibility: visible; top: 38px; left: 92px;"><template shadowrootmode="open"><!----> <div id="content"><slot name="content"></slot></div>
      <!--?lit$641307570$--><!--?--></template>
      <!--?lit$641307570$--><div slot="content"><!----><!--?lit$641307570$--><!----><div><!--?lit$641307570$-->Rename notebook</div><!----><!--?--></div>
    </colab-callout></body></html>
