# BA Skills — Project-level coordination (suggested, not a BA standard)

Use the nine installed skills in `.claude/skills/` **only when relevant**. Do not read them all for every task. The user chooses Coach, Collaborate, Execute or Review explicitly when stated; otherwise infer their intent. Direct execution is the default when the user asks for a deliverable.

## Route by primary deliverable
- BA work plan, choosing method, learning the BA workflow: `ba-coach-workflow`
- Needs, stakeholders, business rules, acceptance criteria or requirements: `business-analysis-requirements`
- UML diagram semantics or choice: `uml-modeling`
- BPMN process, AS-IS/TO-BE and exception flow: `bpmn-process-analyst`
- BA document writing, reorganization and reader clarity: `ba-documentation-communication`
- Source investigation, factual accuracy, standards and competing evidence: `research-evidence-analysis`
- Market alternatives, vendors, build/buy and decision comparisons: `solution-market-research`
- Academic study, literature, research methods and academic writing: `academic-research-writing`
- Practice exercises, learner feedback or skill evaluation: `practice-evaluation`

## Composition rules
1. Choose **one primary skill** from the user's actual task, not from incidental keywords. Add at most one or two supporting skills only when their specialist responsibilities materially change the answer. Do not automatically activate the BA coach before a narrow request.
2. A document requiring new business behavior: requirements owns correctness; documentation owns communication. A rewrite of already approved content: documentation owns and requirements supports only to resolve ambiguity; never silently change a requirement.
3. Process questions: BPMN owns inter-participant flows. UML owns object/system interaction and structural modeling. If both are necessary, first clarify process responsibility, then model necessary system behavior. Do not duplicate diagrams.
4. Solution selection: solution-market owns alternatives and tradeoffs; research-evidence checks material source claims; requirements supplies explicit evaluation criteria where needed.
5. Academic output: academic research owns research methodology/argument; evidence verifies sources; documentation skill need not be triggered just to polish ordinary academic prose.
6. Evaluation is a **separate requested activity**, not an obligatory review of every answer; it never certifies its own effectiveness.
7. Read provided project documents and identify authoritative versions before editing. Protect baseline, IDs, facts, citations and approved decisions. Distinguish official standards, common practice, course/project conventions and AI recommendations.
8. Start with the answer or requested artifact, not metadata or a requirements register. Use tables, traceability and status labels only when they assist a material decision. Surface uncertainties when they affect consequential conclusions.
9. If the user asks to do it now, deliver the work without unnecessary coaching. Never claim to have consulted a source, validated a model, run a tool or tested Claude behavior unless that actually happened.

More routing examples and collision handling: `INTEGRATION_GUIDE.md`.
