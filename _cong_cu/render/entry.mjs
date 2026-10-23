import { convert } from './drawio2svg/lib/index.ts';
window.d2s = (xml) => convert(xml, {backgroundColor:'#ffffff', padding:12, fontFamily:'Arial'});
