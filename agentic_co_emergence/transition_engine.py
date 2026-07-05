from __future__ import annotations

from dataclasses import dataclass, replace

from agentic_co_emergence.models.discussion_event import DiscussionEvent
from agentic_co_emergence.models.discussion_state import DiscussionState


@dataclass
class DiscussionTransitionEngine:
    state: DiscussionState

    def current_state(self) -> DiscussionState:
        return self.state

    def step(self, event: DiscussionEvent) -> DiscussionState:
        if event.kind == "noop":
            return self.state

        if event.kind == "agent_contribution":
            record = {
                "agent_name": event.payload["agent_name"],
                "contribution": event.payload["contribution"],
            }

            self.state = replace(
                self.state,
                transcript=[*self.state.transcript, record],
            )
            return self.state

        raise ValueError(f"Unsupported discussion event kind: {event.kind}")