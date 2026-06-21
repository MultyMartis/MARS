import { readFileSync } from "fs";

const d = JSON.parse(
  readFileSync(
    String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_full_page_discovery_v1.json`,
    "utf8",
  ),
);

for (const s of d.sectionRegister) {
  console.log(`---${s.sectionId}`);
  console.log(`Name: ${s.name}`);
  console.log(
    `Frame: ${s.frameId} | Bounds: x=${s.x} y=${s.y} w=${s.width} h=${s.height} | children: ${s.childrenCount}`,
  );
  console.log(`Groups: ${s.groupRegister.length}`);
  for (const g of s.groupRegister) {
    const flags = [g.autoLayout ? "AL" : "", g.isInstance ? "INST" : ""]
      .filter(Boolean)
      .join(",");
    console.log(
      `  ${g.groupId} | ${g.figName} | ${g.frameId} | ${g.type} | ${g.x},${g.y} ${g.width}x${g.height} | ch:${g.childrenCount}${flags ? " " + flags : ""}`,
    );
  }
}
