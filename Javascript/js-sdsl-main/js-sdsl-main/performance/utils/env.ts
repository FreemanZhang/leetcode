import os from 'os';

export default function getEnv() {
  const v8Version = process.versions.v8;
  const nodeVersion = process.versions.node;
  const plat =
    `${os.type()} ${os.release()} ${os.arch()}
Node.JS ${nodeVersion}
V8 ${v8Version}`;

  const cpus = os.cpus().map(function (cpu) {
    return cpu.model;
  }).reduce(function (o, model) {
    if (!o[model]) o[model] = 0;
    o[model]++;
    return o;
  }, {} as { [key: string]: number });

  return `This is Js-sdsl performance test.

Automatically generated by [github action](https://github.com/js-sdsl/js-sdsl/actions/workflows/build.yml).

To get source code you can go to [github](https://github.com/js-sdsl/js-sdsl/tree/main/performance).

## Environment

\`\`\`bash
${plat}
${Object.keys(cpus).map(function (key) {
    return key + ' \u00d7 ' + cpus[key];
  }).join('\n')}
\`\`\`\n`;
}
